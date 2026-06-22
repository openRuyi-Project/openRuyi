# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quick-xml
%global full_version 0.26.0
%global pkgname quick-xml-0.26

Name:           rust-quick-xml-0.26
Version:        0.26.0
Release:        %autorelease
Summary:        Rust crate "quick-xml"
License:        MIT
URL:            https://github.com/tafia/quick-xml
#!RemoteAsset:  sha256:7f50b1c63b38611e7d4d7f68b82d3ad0cc71a2ad2e7f61fc10f1328d917c93cd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/escape-html) = %{version}
Provides:       crate(%{pkgname}/overlapped-lists) = %{version}

%description
Source code for takopackized Rust crate "quick-xml"

%package     -n %{name}+document-features
Summary:        High performance xml reader and writer - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encoding-rs
Summary:        High performance xml reader and writer - feature "encoding_rs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-rs-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/encoding) = %{version}
Provides:       crate(%{pkgname}/encoding-rs) = %{version}

%description -n %{name}+encoding-rs
This metapackage enables feature "encoding_rs" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "encoding" feature.

%package     -n %{name}+serde
Summary:        High performance xml reader and writer - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.100
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serialize" feature.

%package     -n %{name}+tokio
Summary:        High performance xml reader and writer - feature "tokio" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.0.0
Provides:       crate(%{pkgname}/async-tokio) = %{version}
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust quick-xml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "async-tokio" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
