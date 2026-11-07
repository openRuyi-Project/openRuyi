# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyphenation
%global full_version 0.7.1
%global pkgname hyphenation-0.7

Name:           rust-hyphenation-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "hyphenation"
License:        Apache-2.0 OR MIT
URL:            https://github.com/tapeinosyne/hyphenation
#!RemoteAsset:  sha256:0493c6fb308d367d0aed7acd341adbc1c2f216c135073e4b73b652c5d0d6b54c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atlatl-0.1) >= 0.1.2
Requires:       crate(atlatl-0.1/default) >= 0.1.2
Requires:       crate(atlatl-0.1/serde) >= 0.1.2
Requires:       crate(bincode-1) >= 1.0.0
Requires:       crate(bincode-1/default) >= 1.0.0
Requires:       crate(hyphenation-commons-0.7) >= 0.7.1
Requires:       crate(hyphenation-commons-0.7/default) >= 0.7.1
Requires:       crate(serde-1) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/build-dictionaries) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hyphenation"

%package     -n %{name}+pocket-resources
Summary:        Knuth-Liang hyphenation for a variety of languages - feature "pocket-resources" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pocket-resources-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/embed-all) = %{version}
Provides:       crate(%{pkgname}/pocket-resources) = %{version}

%description -n %{name}+pocket-resources
This metapackage enables feature "pocket-resources" for the Rust hyphenation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "embed_all" feature.

%package     -n %{name}+unicode-normalization
Summary:        Knuth-Liang hyphenation for a variety of languages - feature "unicode-normalization" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-normalization-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/nfc) = %{version}
Provides:       crate(%{pkgname}/nfd) = %{version}
Provides:       crate(%{pkgname}/nfkc) = %{version}
Provides:       crate(%{pkgname}/nfkd) = %{version}
Provides:       crate(%{pkgname}/unicode-normalization) = %{version}

%description -n %{name}+unicode-normalization
This metapackage enables feature "unicode-normalization" for the Rust hyphenation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nfc", "nfd", "nfkc", and "nfkd" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
