# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Ruoqing He <heruoqing@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit      829676e6403ff3fa711c9e901f90f05737c08b88
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global micro_http_commit 876f3feccc30e09225f2c77bf95a6b2d46a9259e

Name:           cloud-hypervisor
Url:            https://github.com/cloud-hypervisor/cloud-hypervisor
Summary:        Cloud Hypervisor is a Virtual Machine Monitor (VMM) that runs on top of KVM
Version:        52.0+git20260608.%{shortcommit}
Release:        %autorelease
License:        Apache-2.0 OR BSD-3-Clause
#!RemoteAsset:  sha256:a2ccccea3efe6b57939f36aa6f1a2acf09cb093427335f657d38d48688fd30b3
Source0:        https://github.com/cloud-hypervisor/cloud-hypervisor/archive/%{commit}/%{name}-%{commit}.tar.gz
#!RemoteAsset:  sha256:1070c3fe63fbd9480b2e1ab1a101b907703bc50e9e598e7bea07d586c93cb8e9
Source1:        https://github.com/firecracker-microvm/micro-http/archive/%{micro_http_commit}/micro-http-%{micro_http_commit}.tar.gz
BuildSystem:    rust

# Redirect micro_http to the packaged local source for reproducible offline builds.
Patch2000:      2000-fix-git-dep.patch

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  binutils
BuildRequires:  pkgconfig(openssl)

BuildRequires:  crate(acpi-tables-0.2/default) >= 0.2.0
BuildRequires:  crate(anyhow-1/default) >= 1.0.102
BuildRequires:  crate(arc-swap-1/default) >= 1.9.1
BuildRequires:  crate(bitfield-struct-0.13/default) >= 0.13.0
BuildRequires:  crate(bitflags-2/default) >= 2.13.0
BuildRequires:  crate(blocking-1/default) >= 1.6.2
BuildRequires:  crate(byteorder-1/default) >= 1.5.0
BuildRequires:  crate(cfg-if-1/default) >= 1.0.4
BuildRequires:  crate(clap-4/cargo) >= 4.6.1
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/string) >= 4.6.1
BuildRequires:  crate(clap-4/wrap-help) >= 4.6.1
BuildRequires:  crate(concat-idents-1/default) >= 1.1.5
BuildRequires:  crate(crc-any-2/default) >= 2.5.0
BuildRequires:  crate(dhat-0.3/default) >= 0.3.3
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.10
BuildRequires:  crate(epoll-4/default) >= 4.4.0
BuildRequires:  crate(fdt-0.1/default) >= 0.1.5
BuildRequires:  crate(flate2-1/default) >= 1.1.9
BuildRequires:  crate(flume-0.12/default) >= 0.12.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.32
BuildRequires:  crate(gdbstub-0.7/default) >= 0.7.10
BuildRequires:  crate(gdbstub-arch-0.3/default) >= 0.3.3
BuildRequires:  crate(getrandom-0.4/default) >= 0.4.2
BuildRequires:  crate(hex-0.4/default) >= 0.4.3
BuildRequires:  crate(iced-x86-1/decoder) >= 1.21.0
BuildRequires:  crate(iced-x86-1/instr-info) >= 1.21.0
BuildRequires:  crate(iced-x86-1/no-d3now) >= 1.21.0
BuildRequires:  crate(iced-x86-1/no-evex) >= 1.21.0
BuildRequires:  crate(iced-x86-1/no-vex) >= 1.21.0
BuildRequires:  crate(iced-x86-1/no-xop) >= 1.21.0
BuildRequires:  crate(iced-x86-1/op-code-info) >= 1.21.0
BuildRequires:  crate(iced-x86-1/std) >= 1.21.0
BuildRequires:  crate(igvm-0.4/default) >= 0.4.0
BuildRequires:  crate(igvm-defs-0.4/default) >= 0.4.0
BuildRequires:  crate(io-uring-0.7/default) >= 0.7.12
BuildRequires:  crate(iommufd-ioctls-0.1/default) >= 0.1.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(jiff-0.2/std) >= 0.2.24
BuildRequires:  crate(kvm-bindings-0.14/default) >= 0.14.0
BuildRequires:  crate(kvm-bindings-0.14/serde) >= 0.14.0
BuildRequires:  crate(kvm-ioctls-0.24/default) >= 0.24.0
BuildRequires:  crate(landlock-0.4/default) >= 0.4.5
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(linux-loader-0.13/bzimage) >= 0.13.2
BuildRequires:  crate(linux-loader-0.13/default) >= 0.13.2
BuildRequires:  crate(linux-loader-0.13/elf) >= 0.13.2
BuildRequires:  crate(linux-loader-0.13/pe) >= 0.13.2
BuildRequires:  crate(log-0.4/default) >= 0.4.30
BuildRequires:  crate(log-0.4/std) >= 0.4.30
BuildRequires:  crate(mshv-bindings-0.6/default) >= 0.6.9
BuildRequires:  crate(mshv-bindings-0.6/fam-wrappers) >= 0.6.9
BuildRequires:  crate(mshv-bindings-0.6/with-serde) >= 0.6.9
BuildRequires:  crate(mshv-ioctls-0.6/default) >= 0.6.9
BuildRequires:  crate(num-enum-0.7/default) >= 0.7.6
BuildRequires:  crate(open-enum-0.5/default) >= 0.5.2
BuildRequires:  crate(pnet-0.35/default) >= 0.35.0
BuildRequires:  crate(pnet-datalink-0.35/default) >= 0.35.0
BuildRequires:  crate(proptest-1/default) >= 1.11.0
BuildRequires:  crate(rand-0.10/default) >= 0.10.1
BuildRequires:  crate(range-map-vec-0.2/default) >= 0.2.0
BuildRequires:  crate(remain-0.2/default) >= 0.2.15
BuildRequires:  crate(seccompiler-0.5/default) >= 0.5.0
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-1/rc) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(serde-with-3/macros) >= 3.20.0
BuildRequires:  crate(sha2-0.11/default) >= 0.11.0
BuildRequires:  crate(signal-hook-0.4/default) >= 0.4.4
BuildRequires:  crate(smallvec-1/default) >= 1.15.1
BuildRequires:  crate(ssh2-0.9/default) >= 0.9.5
BuildRequires:  crate(ssh2-0.9/vendored-openssl) >= 0.9.5
BuildRequires:  crate(tempfile-3/default) >= 3.27.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.18
BuildRequires:  crate(uuid-1/default) >= 1.23.2
BuildRequires:  crate(uuid-1/v4) >= 1.23.2
BuildRequires:  crate(vfio-bindings-0.6/fam-wrappers) >= 0.6.2
BuildRequires:  crate(vfio-ioctls-0.6) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/kvm) >= 0.6.0
BuildRequires:  crate(vfio-ioctls-0.6/vfio-cdev) >= 0.6.0
BuildRequires:  crate(vfio-user-0.1) >= 0.1.3
BuildRequires:  crate(vhost-0.16) >= 0.16.0
BuildRequires:  crate(vhost-0.16/vhost-kern) >= 0.16.0
BuildRequires:  crate(vhost-0.16/vhost-user-backend) >= 0.16.0
BuildRequires:  crate(vhost-0.16/vhost-user-frontend) >= 0.16.0
BuildRequires:  crate(vhost-0.16/vhost-vdpa) >= 0.16.0
BuildRequires:  crate(vhost-user-backend-0.22) >= 0.22.0
BuildRequires:  crate(virtio-bindings-0.2/default) >= 0.2.7
BuildRequires:  crate(virtio-queue-0.17/default) >= 0.17.0
BuildRequires:  crate(vm-fdt-0.3/default) >= 0.3.0
BuildRequires:  crate(vm-memory-0.17/backend-atomic) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/backend-bitmap) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/backend-mmap) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/default) >= 0.17.1
BuildRequires:  crate(vmm-sys-util-0.15/default) >= 0.15.0
BuildRequires:  crate(vmm-sys-util-0.15/with-serde) >= 0.15.0
BuildRequires:  crate(wait-timeout-0.2/default) >= 0.2.1
BuildRequires:  crate(zbus-5/default) >= 5.15.0
BuildRequires:  crate(zerocopy-0.8/alloc) >= 0.8.50
BuildRequires:  crate(zerocopy-0.8/default) >= 0.8.50
BuildRequires:  crate(zerocopy-0.8/derive) >= 0.8.50
BuildRequires:  crate(zstd-0.13/default) >= 0.13.3

Requires:       bash
Requires:       glibc
Requires:       libcap

%ifarch x86_64
%define cargo_pkg_feature_opts --no-default-features --features "mshv,kvm" -p cloud-hypervisor
%endif

%ifarch riscv64
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

%prep -a
# Extract micro-http git dependency to deps/
mkdir -p deps
tar -xf %{SOURCE1} -C deps/
# git+ archives extract to directory named after repo (no version suffix)
if [ -d deps/micro-http ]; then
  : # already exists
elif [ -d deps/micro-http-* ]; then
  mv deps/micro-http-* deps/micro-http
fi

# Create .cargo-checksum.json for git dependency
echo '{"files":{},"package":null}' > deps/micro-http/.cargo-checksum.json

%rust_setup_registry

%build
rm -rf Cargo.lock
export OPENSSL_NO_VENDOR=1

%buildsystem_rust_build -- %{cargo_pkg_feature_opts}
%buildsystem_rust_build -- --package vhost_user_net
%buildsystem_rust_build -- --package vhost_user_block

%install
install -d %{buildroot}%{_bindir}
install -D -m755  ./target/release/cloud-hypervisor %{buildroot}%{_bindir}
install -D -m755  ./target/release/ch-remote %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_libdir}/cloud-hypervisor
install -D -m755 target/release/vhost_user_block %{buildroot}%{_libdir}/cloud-hypervisor
install -D -m755 target/release/vhost_user_net %{buildroot}%{_libdir}/cloud-hypervisor

%check
# Upstream VMM tests require a supported hypervisor such as KVM/MSHV,
# which is not available in the OBS build environment.

%files
%{_bindir}/ch-remote
%caps(cap_net_admin=ep) %{_bindir}/cloud-hypervisor
%dir %{_libdir}/cloud-hypervisor
%{_libdir}/cloud-hypervisor/vhost_user_block
%caps(cap_net_admin=ep) %{_libdir}/cloud-hypervisor/vhost_user_net
%license LICENSES/Apache-2.0.txt
%license LICENSES/BSD-3-Clause.txt
%license LICENSES/CC-BY-4.0.txt

%changelog
%autochangelog
