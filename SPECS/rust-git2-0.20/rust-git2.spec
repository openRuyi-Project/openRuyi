# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git2
%global full_version 0.20.4
%global pkgname git2-0.20

Name:           rust-git2-0.20
Version:        0.20.4
Release:        %autorelease
Summary:        Rust crate "git2"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/git2-rs
#!RemoteAsset:  sha256:7b88256088d75a56f8ecfa070513a775dd9107f6530ef14919dac831af9cfe2b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libgit2-sys-0.18/default) >= 0.18.3
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(url-2.0/default) >= 2.5.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unstable)

%description
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
Source code for takopackized Rust crate "git2"

%package     -n %{name}+default
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/https)
Requires:       crate(%{pkgname}/ssh)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "default" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+https
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "https"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/openssl-probe)
Requires:       crate(%{pkgname}/openssl-sys)
Requires:       crate(libgit2-sys-0.18/https) >= 0.18.3
Provides:       crate(%{pkgname}/https)

%description -n %{name}+https
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "https" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl-probe
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "openssl-probe"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-probe-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/openssl-probe)

%description -n %{name}+openssl-probe
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "openssl-probe" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl-sys
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "openssl-sys"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/default) >= 0.9.112
Provides:       crate(%{pkgname}/openssl-sys)

%description -n %{name}+openssl-sys
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "openssl-sys" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ssh
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "ssh"
Requires:       crate(%{pkgname})
Requires:       crate(libgit2-sys-0.18/ssh) >= 0.18.3
Provides:       crate(%{pkgname}/ssh)

%description -n %{name}+ssh
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "ssh" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored-libgit2
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "vendored-libgit2"
Requires:       crate(%{pkgname})
Requires:       crate(libgit2-sys-0.18/vendored) >= 0.18.3
Provides:       crate(%{pkgname}/vendored-libgit2)

%description -n %{name}+vendored-libgit2
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "vendored-libgit2" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored-openssl
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "vendored-openssl"
Requires:       crate(%{pkgname})
Requires:       crate(libgit2-sys-0.18/vendored-openssl) >= 0.18.3
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.112
Provides:       crate(%{pkgname}/vendored-openssl)

%description -n %{name}+vendored-openssl
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "vendored-openssl" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng-compat
Summary:        Bindings to libgit2 for interoperating with git repositories - feature "zlib-ng-compat"
Requires:       crate(%{pkgname})
Requires:       crate(libgit2-sys-0.18/zlib-ng-compat) >= 0.18.3
Provides:       crate(%{pkgname}/zlib-ng-compat)

%description -n %{name}+zlib-ng-compat
This library is both threadsafe and memory safe and allows both reading and writing git repositories.
This metapackage enables feature "zlib-ng-compat" for the Rust git2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
