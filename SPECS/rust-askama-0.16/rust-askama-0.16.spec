# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name askama
%global full_version 0.16.1
%global pkgname askama-0.16

Name:           rust-askama-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "askama"
License:        MIT OR Apache-2.0
URL:            https://askama.rs/
#!RemoteAsset:  sha256:6024d73179f43f15ccd2b881bfea6fee7f3a46ec53f33b52210dea749ebebaa4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itoa-1/default) >= 1.0.11

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "askama"

%package     -n %{name}+alloc
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-macros-0.16/alloc) >= 0.16.1
Requires:       crate(percent-encoding-2/alloc) >= 2.1.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-json-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+code-in-doc
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "code-in-doc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-macros-0.16/code-in-doc) >= 0.16.1
Provides:       crate(%{pkgname}/code-in-doc) = %{version}

%description -n %{name}+code-in-doc
This metapackage enables feature "code-in-doc" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+config
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-macros-0.16/config) >= 0.16.1
Provides:       crate(%{pkgname}/config) = %{version}

%description -n %{name}+config
This metapackage enables feature "config" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/config) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/urlencode) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-macros-0.16) >= 0.16.1
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/code-in-doc) = %{version}
Requires:       crate(%{pkgname}/default) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly-spans
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "nightly-spans"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-macros-0.16/nightly-spans) >= 0.16.1
Provides:       crate(%{pkgname}/nightly-spans) = %{version}

%description -n %{name}+nightly-spans
This metapackage enables feature "nightly-spans" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(askama-macros-0.16/serde-json) >= 0.16.1
Requires:       crate(serde-1) >= 1.0.0
Requires:       crate(serde-json-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(askama-macros-0.16/std) >= 0.16.1
Requires:       crate(percent-encoding-2/std) >= 2.1.0
Requires:       crate(serde-1/std) >= 1.0.0
Requires:       crate(serde-json-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+urlencode
Summary:        Type-safe, compiled Jinja-like templates for Rust - feature "urlencode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(askama-macros-0.16/urlencode) >= 0.16.1
Requires:       crate(percent-encoding-2) >= 2.1.0
Provides:       crate(%{pkgname}/urlencode) = %{version}

%description -n %{name}+urlencode
This metapackage enables feature "urlencode" for the Rust askama crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
