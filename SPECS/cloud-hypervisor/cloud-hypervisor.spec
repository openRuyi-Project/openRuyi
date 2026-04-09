# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Ruoqing He <heruoqing@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global gitver 50.0
%global gitnum 0

%global obs_packaging_commit 485cd738c50d7be666e2d15ebb57cf029fcc3dd4

Name:           cloud-hypervisor
Url:            https://github.com/cloud-hypervisor/cloud-hypervisor
Summary:        Cloud Hypervisor is a Virtual Machine Monitor (VMM) that runs on top of KVM
Version:        %{gitver}.%{gitnum}
Release:        %autorelease
License:        ASL 2.0 or BSD-3-clause
#!RemoteAsset
Source0:        https://github.com/cloud-hypervisor/obs-packaging/raw/%{obs_packaging_commit}/cloud-hypervisor/src/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/cloud-hypervisor/obs-packaging/raw/%{obs_packaging_commit}/cloud-hypervisor/src/%{name}-%{version}-vendor.tar.gz
#!RemoteAsset
Source2:        https://github.com/cloud-hypervisor/obs-packaging/raw/%{obs_packaging_commit}/cloud-hypervisor/src/config.toml

BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  binutils
BuildRequires:  openssl-devel

BuildRequires:  rust >= 1.88.0
BuildRequires:  cargo >= 1.88.0

Requires: bash
Requires: glibc
Requires: libcap

# TODO: Use rva23 rust toolchain to compile
%ifarch x86_64
%define rust_def_target x86_64-unknown-linux-gnu
%define cargo_pkg_feature_opts --no-default-features --features "mshv,kvm" -p cloud-hypervisor
%endif

%ifarch riscv64
%define rust_def_target riscv64gc-unknown-linux-gnu
%define cargo_pkg_feature_opts --no-default-features --features "kvm" -p cloud-hypervisor
%endif

%define cargo_offline --offline

%description
Cloud Hypervisor is an open source Virtual Machine Monitor (VMM) that runs on
top of KVM. The project focuses on exclusively running modern, cloud workloads,
on top of a limited set of hardware architectures and platforms. Cloud
workloads refers to those that are usually run by customers inside a cloud
provider. For our purposes this means modern Linux* distributions with most I/O
handled by paravirtualised devices (i.e. virtio), no requirement for legacy
devices and recent CPUs and KVM.

%prep

%setup -q
tar xf %{SOURCE1}
mkdir -p .cargo
cp %{SOURCE2} .cargo/

%build
cargo_version=$(cargo --version)
if [[ $? -ne 0 ]]; then
      echo "Cargo not found, please install cargo. exiting"
      exit 0
fi

export OPENSSL_NO_VENDOR=1
cargo build --release --target=%{rust_def_target} %{cargo_pkg_feature_opts} %{cargo_offline}
cargo build --release --target=%{rust_def_target} --package vhost_user_net %{cargo_offline}
cargo build --release --target=%{rust_def_target} --package vhost_user_block %{cargo_offline}

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -D -m755  ./target/%{rust_def_target}/release/cloud-hypervisor %{buildroot}%{_bindir}
install -D -m755  ./target/%{rust_def_target}/release/ch-remote %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_libdir}/cloud-hypervisor
install -D -m755 target/%{rust_def_target}/release/vhost_user_block %{buildroot}%{_libdir}/cloud-hypervisor
install -D -m755 target/%{rust_def_target}/release/vhost_user_net %{buildroot}%{_libdir}/cloud-hypervisor

%files
%defattr(-,root,root,-)
%{_bindir}/ch-remote
%caps(cap_net_admin=ep) %{_bindir}/cloud-hypervisor
%dir %{_libdir}/cloud-hypervisor
%{_libdir}/cloud-hypervisor/vhost_user_block
%caps(cap_net_admin=ep) %{_libdir}/cloud-hypervisor/vhost_user_net
%if 0%{?using_musl_libc}
%{_libdir}/cloud-hypervisor/static/ch-remote
%caps(cap_net_admim=ep) %{_libdir}/cloud-hypervisor/static/cloud-hypervisor
%{_libdir}/cloud-hypervisor/static/vhost_user_block
%caps(cap_net_admin=ep) %{_libdir}/cloud-hypervisor/static/vhost_user_net
%endif
%license LICENSES/Apache-2.0.txt
%license LICENSES/BSD-3-Clause.txt
%license LICENSES/CC-BY-4.0.txt

%changelog
%autochangelog
