# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           virtiofsd
Version:        1.14.0
Release:        %autorelease
Summary:        Virtio-fs vhost-user device daemon
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://gitlab.com/virtio-fs/virtiofsd
#!RemoteAsset:  sha256:52b66e449ca583b4f050a2bff327ff812211a2c349b4130279fcfc6a64540f04
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    rust

# Use Rust crate versions that are already packaged in openRuyi.
Patch2000:      0001-Cargo-use-openRuyi-packaged-compatible-crate-versions.patch

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  crate(bitflags-1/default) >= 1.2.0
BuildRequires:  crate(btree-range-map-0.7/default) >= 0.7.0
BuildRequires:  crate(capng-0.2/default) >= 0.2.2
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.0
BuildRequires:  crate(futures-0.3/thread-pool) >= 0.3.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.177
BuildRequires:  crate(libseccomp-sys-0.2/default) >= 0.2.1
BuildRequires:  crate(log-0.4/default) >= 0.4.0
BuildRequires:  crate(postcard-1/default) >= 1.0.0
BuildRequires:  crate(postcard-1/use-std) >= 1.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(syslog-7/default) >= 7.0.0
BuildRequires:  crate(vhost-0.16/default) >= 0.16.0
BuildRequires:  crate(vhost-user-backend-0.22/default) >= 0.22.0
BuildRequires:  crate(virtio-bindings-0.2/default) >= 0.2.7
BuildRequires:  crate(virtio-queue-0.17/default) >= 0.17.0
BuildRequires:  crate(vm-memory-0.17/backend-atomic) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/backend-mmap) >= 0.17.1
BuildRequires:  crate(vm-memory-0.17/default) >= 0.17.1
BuildRequires:  crate(vmm-sys-util-0.15/default) >= 0.15.0

%description
virtiofsd is a vhost-user backend that implements the virtio-fs device. It
allows virtual machines to access a host directory tree with local file system
semantics and is commonly used by lightweight VM and secure-container stacks.

%prep -a
rm -f Cargo.lock

%install
install -Dpm0755 target/release/virtiofsd \
    %{buildroot}%{_libexecdir}/virtiofsd
install -d %{buildroot}%{_bindir}
ln -s ../libexec/virtiofsd %{buildroot}%{_bindir}/virtiofsd
install -Dpm0644 50-virtiofsd.json \
    %{buildroot}%{_datadir}/qemu/vhost-user/50-virtiofsd.json

%check
# The upstream test suite requires privileged namespace, seccomp, and FUSE
# behavior that is not available in a normal OBS package build chroot.

%files
%doc README.md doc/
%license LICENSE-APACHE
%license LICENSE-BSD-3-Clause
%{_bindir}/virtiofsd
%{_libexecdir}/virtiofsd
%dir %{_datadir}/qemu
%dir %{_datadir}/qemu/vhost-user
%{_datadir}/qemu/vhost-user/50-virtiofsd.json

%changelog
%autochangelog
