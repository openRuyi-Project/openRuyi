# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git2
%global full_version 0.21.0
%global pkgname git2-0.21

Name:           rust-git2-0.21
Version:        0.21.0
Release:        %autorelease
Summary:        Rust crate "git2"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/git2-rs
#!RemoteAsset:  sha256:ddddbf932745a6be37109b6112d3ee09696106f848449069d3a57bba937ab82e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.1.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(libgit2-sys-0.18/default) >= 0.18.4
Requires:       crate(log-0.4/default) >= 0.4.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
Source code for takopackized Rust crate "git2"

%package     -n %{name}+cred
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "cred"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(url-2/default) >= 2.5.4
Provides:       crate(%{pkgname}/cred) = %{version}

%description -n %{name}+cred
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "cred" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "https"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cred) = %{version}
Requires:       crate(%{pkgname}/openssl-probe) = %{version}
Requires:       crate(%{pkgname}/openssl-sys) = %{version}
Requires:       crate(libgit2-sys-0.18/https) >= 0.18.4
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
Requires:       crate(%{pkgname}/cred) = %{version}
Requires:       crate(libgit2-sys-0.18/ssh) >= 0.18.4
Provides:       crate(%{pkgname}/ssh) = %{version}

%description -n %{name}+ssh
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "ssh" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-sha256
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "unstable-sha256"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libgit2-sys-0.18/unstable-sha256) >= 0.18.4
Provides:       crate(%{pkgname}/unstable-sha256) = %{version}

%description -n %{name}+unstable-sha256
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "unstable-sha256" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored-libgit2
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "vendored-libgit2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libgit2-sys-0.18/vendored) >= 0.18.4
Provides:       crate(%{pkgname}/vendored-libgit2) = %{version}

%description -n %{name}+vendored-libgit2
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "vendored-libgit2" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored-openssl
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "vendored-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libgit2-sys-0.18/vendored-openssl) >= 0.18.4
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.45
Provides:       crate(%{pkgname}/vendored-openssl) = %{version}

%description -n %{name}+vendored-openssl
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "vendored-openssl" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "zlib-ng-compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libgit2-sys-0.18/zlib-ng-compat) >= 0.18.4
Provides:       crate(%{pkgname}/zlib-ng-compat) = %{version}

%description -n %{name}+zlib-ng-compat
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "zlib-ng-compat" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
