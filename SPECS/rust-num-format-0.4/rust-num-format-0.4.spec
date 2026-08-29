# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-format
%global full_version 0.4.4
%global pkgname num-format-0.4

Name:           rust-num-format-0.4
Version:        0.4.4
Release:        %autorelease
Summary:        Rust crate "num-format"
License:        MIT OR Apache-2.0
URL:            https://github.com/bcmyers/num-format
#!RemoteAsset:  sha256:a652d9771a63711fd3c3deb670acfbe5c30a4072e664d7a3bf5a9e1056ac72c3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7) >= 0.7.2
Requires:       crate(itoa-1) >= 1.0.4
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "num-format"

%package     -n %{name}+cfg-if
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "cfg-if"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cfg-if-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/cfg-if) = %{version}

%description -n %{name}+cfg-if
This metapackage enables feature "cfg-if" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encoding-rs
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "encoding_rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-rs-0.8/default) >= 0.8.31
Provides:       crate(%{pkgname}/encoding-rs) = %{version}

%description -n %{name}+encoding-rs
This metapackage enables feature "encoding_rs" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lazy-static
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "lazy_static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lazy-static-1/default) >= 1.4.0
Provides:       crate(%{pkgname}/lazy-static) = %{version}

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.134
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-format-windows
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "num-format-windows"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-format-windows-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/num-format-windows) = %{version}

%description -n %{name}+num-format-windows
This metapackage enables feature "num-format-windows" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.145
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7/default) >= 0.7.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+widestring
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "widestring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(widestring-1/default) >= 1.0.2
Provides:       crate(%{pkgname}/widestring) = %{version}

%description -n %{name}+widestring
This metapackage enables feature "widestring" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+winapi
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "winapi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/winnls) >= 0.3.9
Provides:       crate(%{pkgname}/winapi) = %{version}

%description -n %{name}+winapi
This metapackage enables feature "winapi" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-num-bigint
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "with-num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-bigint) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/with-num-bigint) = %{version}

%description -n %{name}+with-num-bigint
This metapackage enables feature "with-num-bigint" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-serde
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "with-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7/serde) >= 0.7.2
Requires:       crate(serde-1/derive) >= 1.0.145
Provides:       crate(%{pkgname}/with-serde) = %{version}

%description -n %{name}+with-serde
This metapackage enables feature "with-serde" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-system-locale
Summary:        Producing string-representations of numbers, formatted according to international standards - feature "with-system-locale"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cfg-if) = %{version}
Requires:       crate(%{pkgname}/encoding-rs) = %{version}
Requires:       crate(%{pkgname}/lazy-static) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/num-format-windows) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/widestring) = %{version}
Requires:       crate(winapi-0.3/winnls) >= 0.3.9
Provides:       crate(%{pkgname}/with-system-locale) = %{version}

%description -n %{name}+with-system-locale
This metapackage enables feature "with-system-locale" for the Rust num-format crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
