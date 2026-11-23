# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name askama_derive
%global full_version 0.16.1
%global pkgname askama-derive-0.16

Name:           rust-askama-derive-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "askama_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/askama-rs/askama
#!RemoteAsset:  sha256:071ee5ebf2138e3ad180e0aacf6940c2cab5e6d8333741d9925c7bee2b153f39
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(askama-parser-0.16/default) >= 0.16.1
Requires:       crate(memchr-2/default) >= 2.0.0
Requires:       crate(proc-macro2-1) >= 1.0.0
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(rustc-hash-2/default) >= 2.0.0
Requires:       crate(syn-3/clone-impls) >= 3.0.0
Requires:       crate(syn-3/derive) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0
Requires:       crate(syn-3/parsing) >= 3.0.0
Requires:       crate(syn-3/printing) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/external-sources) = %{version}
Provides:       crate(%{pkgname}/nightly-spans) = %{version}
Provides:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/urlencode) = %{version}

%description
Source code for takopackized Rust crate "askama_derive"

%package     -n %{name}+code-in-doc
Summary:        Code generator of Askama templating engine - feature "code-in-doc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pulldown-cmark-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/code-in-doc) = %{version}

%description -n %{name}+code-in-doc
This metapackage enables feature "code-in-doc" for the Rust askama_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+config
Summary:        Code generator of Askama templating engine - feature "config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/external-sources) = %{version}
Requires:       crate(askama-parser-0.16/config) >= 0.16.1
Requires:       crate(basic-toml-0.1/default) >= 0.1.1
Requires:       crate(glob-0.3/default) >= 0.3.3
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/config) = %{version}

%description -n %{name}+config
This metapackage enables feature "config" for the Rust askama_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Code generator of Askama templating engine - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/code-in-doc) = %{version}
Requires:       crate(%{pkgname}/config) = %{version}
Requires:       crate(%{pkgname}/external-sources) = %{version}
Requires:       crate(%{pkgname}/proc-macro) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/urlencode) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust askama_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro
Summary:        Code generator of Askama templating engine - feature "proc-macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-1/proc-macro) >= 1.0.0
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description -n %{name}+proc-macro
This metapackage enables feature "proc-macro" for the Rust askama_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
