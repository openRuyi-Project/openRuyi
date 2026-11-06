# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libpathrs
Version:        0.2.6
Release:        %autorelease
Summary:        Safe path resolution on Linux
License:        MPL-2.0 OR LGPL-3.0-or-later
URL:            https://github.com/cyphar/libpathrs
#!RemoteAsset:  sha256:6aac480634e9b1dd8a74db4022dbb2ae70208fe5335f4d25345513ac53dbf3e9
Source0:        https://github.com/cyphar/libpathrs/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  lld
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.63
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(bitflags-2/default) >= 2.13
BuildRequires:  crate(bitflags-2/bytemuck) >= 2.13
BuildRequires:  crate(bytemuck-1/default)
BuildRequires:  crate(bytemuck-1/derive)
BuildRequires:  crate(bytemuck-1/extern-crate-std)
BuildRequires:  crate(itertools-0.15/default)
BuildRequires:  crate(libc-0.2/default) >= 0.2.183
BuildRequires:  crate(memchr-2/default)
BuildRequires:  crate(once-cell-1/default)
BuildRequires:  crate(open-enum-0.3/default)
BuildRequires:  crate(rand-0.9/default)
BuildRequires:  crate(rustix-1/default) >= 1.1
BuildRequires:  crate(rustix-1/fs) >= 1.1
BuildRequires:  crate(rustix-1/mount) >= 1.1
BuildRequires:  crate(rustix-1/process) >= 1.1
BuildRequires:  crate(rustix-1/system) >= 1.1
BuildRequires:  crate(rustix-1/thread) >= 1.1
BuildRequires:  crate(rustversion-1/default)
BuildRequires:  crate(static-assertions-1/default) >= 1.1
BuildRequires:  crate(tempfile-3/default)
BuildRequires:  crate(thiserror-2/default)
# Keep the development dependencies of the library and both workspace members.
BuildRequires:  crate(anyhow-1/default)
BuildRequires:  crate(bpfvm-0.1/default)
BuildRequires:  crate(clap-3/cargo)
BuildRequires:  crate(clap-3/default)
BuildRequires:  crate(clap-4/default)
BuildRequires:  crate(clap-4/string)
BuildRequires:  crate(errno-0.3/default)
BuildRequires:  crate(indoc-2/default)
BuildRequires:  crate(paste-1/default)
BuildRequires:  crate(path-clean-1/default)
BuildRequires:  crate(pretty-assertions-1/default) >= 1.4.1
BuildRequires:  crate(pretty-assertions-1/unstable) >= 1.4.1
BuildRequires:  crate(scopeguard-1/default)
BuildRequires:  crate(syscalls-0.8/default)

%description
Libpathrs provides safe path resolution and filesystem operations on Linux
through a C API, with support for openat2 and procfs-based operations.

%package devel
Summary:        Development files for libpathrs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers, the shared-library linker symlink, and pkg-config metadata for
building programs and language bindings against libpathrs.

%package static
Summary:        Static library for libpathrs
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The static libpathrs library for applications that require static linking.

%prep
# The VCS archive has one top-level directory; keep the complete workspace.
%autosetup -n %{name}-%{version}
%rust_setup_registry
# Resolve against the packaged registry instead of the upstream lockfile.
rm -f Cargo.lock

%build
# Upstream builds the shared and static C APIs separately to set symbol
# versions and the SONAME. Use clang and lld on both supported architectures.
make release CARGO="cargo --offline" EXTRA_RUSTC_FLAGS="-C linker=clang"

%install
./install.sh DESTDIR=%{buildroot} --prefix=%{_prefix} --libdir=%{_libdir}

%check
# Run all workspace members, library tests, examples, and doctests with the
# C API enabled; privileged tests remain subject to upstream's feature gates.
cargo test --offline --workspace --features capi

%files
%doc README.md CHANGELOG.md INSTALL.md COPYING.md
%license LICENSE.MPL-2.0 LICENSE.LGPL-3.0 LICENSE.GPL-3.0
%{_libdir}/libpathrs.so.0
%{_libdir}/libpathrs.so.%{version}

%files devel
%{_includedir}/pathrs.h
%{_libdir}/libpathrs.so
%{_libdir}/pkgconfig/pathrs.pc

%files static
%{_libdir}/libpathrs.a

%changelog
%autochangelog
