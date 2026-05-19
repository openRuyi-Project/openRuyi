# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quick-xml
%global full_version 0.38.4
%global pkgname quick-xml-0.38

Name:           rust-quick-xml-0.38
Version:        0.38.4
Release:        %autorelease
Summary:        Rust crate "quick-xml"
License:        MIT
URL:            https://github.com/tafia/quick-xml
#!RemoteAsset:  sha256:b66c2058c55a409d601666cffe35f04333cf1013010882cec174a7467cd4e21c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0/default) >= 2.8.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/escape-html)
Provides:       crate(%{pkgname}/overlapped-lists)

%description
Source code for takopackized Rust crate "quick-xml"

%package     -n %{name}+arbitrary
Summary:        High performance xml reader and writer - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Requires:       crate(arbitrary-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        High performance xml reader and writer - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encoding-rs
Summary:        High performance xml reader and writer - feature "encoding_rs" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(encoding-rs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/encoding)
Provides:       crate(%{pkgname}/encoding-rs)

%description -n %{name}+encoding-rs
This metapackage enables feature "encoding_rs" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "encoding" feature.

%package     -n %{name}+serde
Summary:        High performance xml reader and writer - feature "serde" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.139
Provides:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/serialize)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serialize" feature.

%package     -n %{name}+serde-types
Summary:        High performance xml reader and writer - feature "serde-types"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.139
Provides:       crate(%{pkgname}/serde-types)

%description -n %{name}+serde-types
This metapackage enables feature "serde-types" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        High performance xml reader and writer - feature "tokio" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/io-util) >= 1.10
Provides:       crate(%{pkgname}/async-tokio)
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "async-tokio" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
