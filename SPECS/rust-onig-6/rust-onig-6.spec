# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name onig
%global full_version 6.5.3
%global pkgname onig-6

Name:           rust-onig-6
Version:        6.5.3
Release:        %autorelease
Summary:        Rust crate "onig"
License:        MIT
URL:            https://github.com/iwillspeak/rust-onig
#!RemoteAsset:  sha256:0cc3cbf698f9438986c11a880c90a6d04b9de27575afd28bbf45b154b6c709e2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(once-cell-1/default) >= 1.12.0
Requires:       crate(onig-sys-69) >= 69.9.3
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std-pattern) = %{version}

%description
Oniguruma is a modern regex library with support for multiple character encodings and regex syntaxes.
Source code for takopackized Rust crate "onig"

%package     -n %{name}+generate
Summary:        Rust-Onig is a set of Rust bindings for the Oniguruma regular expression library - feature "generate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(onig-sys-69/generate) >= 69.9.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/generate) = %{version}

%description -n %{name}+generate
Oniguruma is a modern regex library with support for multiple character encodings and regex syntaxes.
This metapackage enables feature "generate" for the Rust onig crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+posix-api
Summary:        Rust-Onig is a set of Rust bindings for the Oniguruma regular expression library - feature "posix-api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(onig-sys-69/posix-api) >= 69.9.3
Provides:       crate(%{pkgname}/posix-api) = %{version}

%description -n %{name}+posix-api
Oniguruma is a modern regex library with support for multiple character encodings and regex syntaxes.
This metapackage enables feature "posix-api" for the Rust onig crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+print-debug
Summary:        Rust-Onig is a set of Rust bindings for the Oniguruma regular expression library - feature "print-debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(onig-sys-69/print-debug) >= 69.9.3
Provides:       crate(%{pkgname}/print-debug) = %{version}

%description -n %{name}+print-debug
Oniguruma is a modern regex library with support for multiple character encodings and regex syntaxes.
This metapackage enables feature "print-debug" for the Rust onig crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
