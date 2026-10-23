# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           kata-containers
Version:        4.2.0
Release:        %autorelease
Summary:        Secure container runtime with lightweight virtual machines
License:        Apache-2.0
URL:            https://github.com/kata-containers/kata-containers
#!RemoteAsset:  sha256:550542a1d053657807fe883185ce041bab1540229ef89c5d5ea4b82c91fd6b8c
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:8e27ae072cd50f50ce8337820c6d32091899ff342f3d04355c659fdb7dd3eacd
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}-vendor.tar.gz
# Kata's runtime is built through upstream Go Makefiles; the Rust agent is built
# in the same package because Kata ships both components together.
BuildSystem:    golang

BuildRequires:  cargo >= 1.96.0
BuildRequires:  git
BuildRequires:  go >= 1.26.7
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  make
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  rust >= 1.96.0
BuildRequires:  rust-rpm-macros

Recommends:     virtiofsd

Requires:       cloud-hypervisor

%patchlist
# Poll sysfs while waiting for PCI network devices so Cloud Hypervisor hotplug
# does not stall when the uevent watcher misses an already-created netdev.
0001-agent-poll-sysfs-while-waiting-for-PCI-net-devices.patch
# Increase the Cloud Hypervisor CreateVM and BootVM timeout on riscv64, where
# nested virtualization under QEMU/TCG boots more slowly during validation.
0002-virtcontainers-extend-Cloud-Hypervisor-boot-timeout-.patch
# Register Cloud Hypervisor as an available riscv64 hypervisor in Kata's
# architecture options so DEFAULT_HYPERVISOR=cloud-hypervisor is accepted.
0003-runtime-enable-Cloud-Hypervisor-config-on-RISC-V.patch
# Ensure the optimized kata-agent build generates src/version.rs before Cargo
# compiles the binary.
0004-agent-generate-version-file-for-optimized-builds.patch
# Resolve the platform PCI root bus path used by RISC-V virt machines without
# ACPI, falling back to /devices/platform/.../pci0000:* when needed.
2000-agent-resolve-RISC-V-platform-PCI-root-bus-path.patch

%description
Kata Containers provides a secure container runtime using lightweight virtual
machines. It integrates with OCI and CRI runtimes while improving workload
isolation with a dedicated guest kernel and agent.

%prep
%autosetup -p1
tar -xf %{SOURCE1}
cat >> .cargo/config.toml <<EOF
[net]
offline = true
EOF

%build
export GOFLAGS="-mod=vendor"
rust_host_triple="$(rustc -vV | sed -n 's/^host: //p')"
make -C src/runtime \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    DEFAULT_HYPERVISOR=cloud-hypervisor

make -C src/agent \
    BUILD_TYPE=release \
    TRIPLE="${rust_host_triple}" \
    optimize

%install
export GOFLAGS="-mod=vendor"
rust_host_triple="$(rustc -vV | sed -n 's/^host: //p')"
make -C src/runtime \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    DEFAULT_HYPERVISOR=cloud-hypervisor \
    install

install -Dpm0755 target/${rust_host_triple}/release/kata-agent \
    %{buildroot}%{_datadir}/kata-containers/kata-agent

%check
# Upstream tests require nested virtualization, container runtime state, or
# privileged kernel features that are unavailable in a normal package chroot.

%files
%doc README.md VERSION
%license LICENSE
%{_bindir}/kata-runtime
%{_bindir}/containerd-shim-kata-v2
%{_bindir}/kata-monitor
%{_bindir}/kata-collect-data.sh
%{_datadir}/bash-completion/completions/kata-runtime
%{_datadir}/defaults/kata-containers/
%{_datadir}/kata-containers/kata-agent

%changelog
%autochangelog
