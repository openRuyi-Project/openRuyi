# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Ruoqing He <heruoqing@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream_commit 1e18716fbdc01df4538bb1604f6019d95ed29da3
%global vendor_dir %{name}-%{version}-vendor

Name:           cloud-hypervisor
Version:        52.0.0+git20260602.1e18716
Release:        %autorelease
Summary:        Virtual Machine Monitor that runs on top of KVM
License:        (Apache-2.0 OR BSD-3-Clause) AND CC-BY-4.0
URL:            https://github.com/cloud-hypervisor/cloud-hypervisor
#!RemoteAsset:  sha256:c65f8ca029c5f84d305fd1e5bb5a540fc1a0c178111bd0a1d817985c457014c9
Source0:        https://codeload.github.com/cloud-hypervisor/cloud-hypervisor/tar.gz/%{upstream_commit}#/%{name}-%{version}.tar.gz
# Generated from Source0 with `cargo vendor --locked --versioned-dirs`.
#!RemoteAsset:  sha256:442624c499f0ee7c41d00f2645161c31cd55bc963c54354a3ed50090f92ace5b
Source1:        https://github.com/wangyf0611/cloud-hypervisor/releases/download/openruyi-vendor-52.0.0-git20260602-1e18716/%{name}-%{version}-vendor.tar.zst

BuildSystem:    rust

BuildRequires:  binutils
BuildRequires:  cargo >= 1.89.0
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  rust >= 1.89.0
BuildRequires:  rust-rpm-macros
BuildRequires:  zstd

Requires:       bash
Requires:       glibc
Requires:       libcap

%ifarch x86_64
%define rust_def_target x86_64-unknown-linux-gnu
%define cargo_pkg_feature_opts --no-default-features --features "mshv,kvm" -p cloud-hypervisor
%endif

%ifarch riscv64
%define rust_def_target riscv64gc-unknown-linux-gnu
%define cargo_pkg_feature_opts --no-default-features --features "kvm" -p cloud-hypervisor
%endif

%description
Cloud Hypervisor is an open source Virtual Machine Monitor (VMM) that runs on
top of KVM. The project focuses on exclusively running modern, cloud workloads,
on top of a limited set of hardware architectures and platforms. Cloud
workloads refers to those that are usually run by customers inside a cloud
provider. For our purposes this means modern Linux* distributions with most I/O
handled by paravirtualised devices (i.e. virtio), no requirement for legacy
devices and recent CPUs and KVM.

%prep
%autosetup -n %{name}-%{upstream_commit}
tar -I zstd -xf %{SOURCE1}
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/firecracker-microvm/micro-http?branch=main"]
git = "https://github.com/firecracker-microvm/micro-http"
branch = "main"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "%{vendor_dir}"

[net]
offline = true
EOF

%build
export OPENSSL_NO_VENDOR=1
cargo build --release --locked --offline --target=%{rust_def_target} %{cargo_pkg_feature_opts}
cargo build --release --locked --offline --target=%{rust_def_target} --package vhost_user_net
cargo build --release --locked --offline --target=%{rust_def_target} --package vhost_user_block

%install
install -Dpm0755 target/%{rust_def_target}/release/cloud-hypervisor %{buildroot}%{_bindir}/cloud-hypervisor
install -Dpm0755 target/%{rust_def_target}/release/ch-remote %{buildroot}%{_bindir}/ch-remote
install -Dpm0755 target/%{rust_def_target}/release/vhost_user_block %{buildroot}%{_libdir}/cloud-hypervisor/vhost_user_block
install -Dpm0755 target/%{rust_def_target}/release/vhost_user_net %{buildroot}%{_libdir}/cloud-hypervisor/vhost_user_net

%check
# The upstream test suite requires KVM-capable hosts and is not suitable for
# the generic OBS build workers.

%files
%doc README.md
%license LICENSES/Apache-2.0.txt
%license LICENSES/BSD-3-Clause.txt
%license LICENSES/CC-BY-4.0.txt
%{_bindir}/ch-remote
%caps(cap_net_admin=ep) %{_bindir}/cloud-hypervisor
%dir %{_libdir}/cloud-hypervisor
%{_libdir}/cloud-hypervisor/vhost_user_block
%caps(cap_net_admin=ep) %{_libdir}/cloud-hypervisor/vhost_user_net

%changelog
%autochangelog
