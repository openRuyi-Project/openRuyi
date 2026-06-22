# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyphenation
%global full_version 0.8.4
%global pkgname hyphenation-0.8

Name:           rust-hyphenation-0.8
Version:        0.8.4
Release:        %autorelease
Summary:        Rust crate "hyphenation"
License:        Apache-2.0 OR MIT
URL:            https://github.com/tapeinosyne/hyphenation
#!RemoteAsset:  sha256:bcf4dd4c44ae85155502a52c48739c8a48185d1449fff1963cffee63c28a50f0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bincode-1) >= 1.3.3
Requires:       crate(bincode-1/default) >= 1.3.3
Requires:       crate(fst-0.4) >= 0.4.6
Requires:       crate(fst-0.4/default) >= 0.4.6
Requires:       crate(hyphenation-commons-0.8) >= 0.8.4
Requires:       crate(hyphenation-commons-0.8/default) >= 0.8.4
Requires:       crate(serde-1) >= 1.0.126
Requires:       crate(serde-1/default) >= 1.0.126
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/build-dictionaries) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hyphenation"

%package     -n %{name}+pocket-resources
Summary:        Knuth-Liang hyphenation for a variety of languages - feature "pocket-resources" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pocket-resources-0.3/default) >= 0.3.2
Provides:       crate(%{pkgname}/embed-all) = %{version}
Provides:       crate(%{pkgname}/embed-en-us) = %{version}
Provides:       crate(%{pkgname}/pocket-resources) = %{version}

%description -n %{name}+pocket-resources
This metapackage enables feature "pocket-resources" for the Rust hyphenation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "embed_all", and "embed_en-us" features.

%package     -n %{name}+unicode-normalization
Summary:        Knuth-Liang hyphenation for a variety of languages - feature "unicode-normalization" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-normalization-0.1/default) >= 0.1.19
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
