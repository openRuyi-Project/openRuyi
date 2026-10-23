# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git2
%global full_version 0.19.0
%global pkgname git2-0.19

Name:           rust-git2-0.19
Version:        0.19.0
Release:        %autorelease
Summary:        Rust crate "git2"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/git2-rs
#!RemoteAsset:  sha256:b903b73e45dc0c6c596f2d37eccece7c1c8bb6e4407b001096387c63d0d93724
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.1.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(libgit2-sys-0.17/default) >= 0.17.0
Requires:       crate(log-0.4/default) >= 0.4.8
Requires:       crate(url-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
Source code for takopackized Rust crate "git2"

%package     -n %{name}+default
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/https) = %{version}
Requires:       crate(%{pkgname}/ssh) = %{version}
Requires:       crate(%{pkgname}/ssh-key-from-memory) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "default" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "https"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/openssl-probe) = %{version}
Requires:       crate(%{pkgname}/openssl-sys) = %{version}
Requires:       crate(libgit2-sys-0.17/https) >= 0.17.0
Provides:       crate(%{pkgname}/https) = %{version}

%description -n %{name}+https
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "https" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl-probe
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "openssl-probe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-probe-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/openssl-probe) = %{version}

%description -n %{name}+openssl-probe
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "openssl-probe" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl-sys
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "openssl-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-sys-0.9/default) >= 0.9.45
Provides:       crate(%{pkgname}/openssl-sys) = %{version}

%description -n %{name}+openssl-sys
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "openssl-sys" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ssh
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "ssh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libgit2-sys-0.17/ssh) >= 0.17.0
Provides:       crate(%{pkgname}/ssh) = %{version}

%description -n %{name}+ssh
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "ssh" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ssh-key-from-memory
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "ssh_key_from_memory"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libgit2-sys-0.17/ssh-key-from-memory) >= 0.17.0
Provides:       crate(%{pkgname}/ssh-key-from-memory) = %{version}

%description -n %{name}+ssh-key-from-memory
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "ssh_key_from_memory" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored-libgit2
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "vendored-libgit2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libgit2-sys-0.17/vendored) >= 0.17.0
Provides:       crate(%{pkgname}/vendored-libgit2) = %{version}

%description -n %{name}+vendored-libgit2
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "vendored-libgit2" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored-openssl
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "vendored-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libgit2-sys-0.17/vendored-openssl) >= 0.17.0
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.45
Provides:       crate(%{pkgname}/vendored-openssl) = %{version}

%description -n %{name}+vendored-openssl
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "vendored-openssl" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "zlib-ng-compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libgit2-sys-0.17/zlib-ng-compat) >= 0.17.0
Provides:       crate(%{pkgname}/zlib-ng-compat) = %{version}

%description -n %{name}+zlib-ng-compat
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "zlib-ng-compat" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
