# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: isrc-riscv-port <riscv-port@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%ifarch x86_64
%global rust_def_target x86_64-unknown-linux-gnu
%endif

%ifarch riscv64
%global rust_def_target riscv64gc-unknown-linux-gnu
%endif

Name:           kata-containers
Version:        3.29.0
Release:        %autorelease
Summary:        Secure container runtime with lightweight virtual machines
License:        Apache-2.0
URL:            https://github.com/kata-containers/kata-containers
#!RemoteAsset:  sha256:8dab047ee17d2cd2fc8cdb01d2530c65cd2235e48e964c95a9a3a9275f721078
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Kata combines a Go runtime and Rust agent behind upstream custom Makefiles.
# The available declarative build systems do not cover this mixed build yet.
BuildSystem:

BuildRequires:  cargo >= 1.92.0
BuildRequires:  git
BuildRequires:  go >= 1.25.9
BuildRequires:  go-rpm-macros
BuildRequires:  make
BuildRequires:  rust >= 1.92.0
BuildRequires:  rust-rpm-macros

Requires:       cloud-hypervisor
Requires:       virtiofsd

%patchlist
# Poll sysfs while waiting for PCI network devices so Cloud Hypervisor hotplug
# does not stall when the uevent watcher misses an already-created netdev.
0001-agent-poll-sysfs-while-waiting-for-PCI-net-devices.patch
# Resolve the platform PCI root bus path used by RISC-V virt machines without
# ACPI, falling back to /devices/platform/.../pci0000:* when needed.
0002-agent-resolve-RISC-V-platform-PCI-root-bus-path.patch
# Increase the Cloud Hypervisor CreateVM and BootVM timeout on riscv64, where
# nested virtualization under QEMU/TCG boots more slowly during validation.
0003-virtcontainers-extend-Cloud-Hypervisor-boot-timeout-.patch
# Register Cloud Hypervisor as an available riscv64 hypervisor in Kata's
# architecture options so DEFAULT_HYPERVISOR=cloud-hypervisor is accepted.
0004-runtime-enable-Cloud-Hypervisor-config-on-RISC-V.patch

%description
Kata Containers provides a secure container runtime using lightweight virtual
machines. It integrates with OCI and CRI runtimes while improving workload
isolation with a dedicated guest kernel and agent.

%prep
%autosetup -p1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"

[net]
offline = true
EOF

%build
export GOFLAGS="-mod=vendor"
make -C src/runtime \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    DEFAULT_HYPERVISOR=cloud-hypervisor

make -C src/agent \
    BUILD_TYPE=release \
    TRIPLE=%{rust_def_target} \
    optimize

%install
export GOFLAGS="-mod=vendor"
make -C src/runtime \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    DEFAULT_HYPERVISOR=cloud-hypervisor \
    install

install -Dpm0755 target/%{rust_def_target}/release/kata-agent \
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
