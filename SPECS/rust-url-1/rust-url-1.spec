# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name url
%global full_version 1.7.2
%global pkgname url-1

Name:           rust-url-1
Version:        1.7.2
Release:        %autorelease
Summary:        Rust crate "url"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url
#!RemoteAsset:  sha256:dd4e7c0d531266369519a4aa4f399d748bd37043b00bde1e4ff1f60a120b355a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(idna-0.1/default) >= 0.1.0
Requires:       crate(matches-0.1/default) >= 0.1.0
Requires:       crate(percent-encoding-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "url"

%package     -n %{name}+encoding
Summary:        URL library for Rust, based on the WHATWG URL Standard - feature "encoding" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(encoding-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/encoding) = %{version}
Provides:       crate(%{pkgname}/query-encoding) = %{version}

%description -n %{name}+encoding
This metapackage enables feature "encoding" for the Rust url crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "query_encoding" feature.

%package     -n %{name}+heapsize
Summary:        URL library for Rust, based on the WHATWG URL Standard - feature "heapsize" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heapsize-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/heap-size) = %{version}
Provides:       crate(%{pkgname}/heapsize) = %{version}

%description -n %{name}+heapsize
This metapackage enables feature "heapsize" for the Rust url crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "heap_size" feature.

%package     -n %{name}+rustc-serialize
Summary:        URL library for Rust, based on the WHATWG URL Standard - feature "rustc-serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-serialize-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/rustc-serialize) = %{version}

%description -n %{name}+rustc-serialize
This metapackage enables feature "rustc-serialize" for the Rust url crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        URL library for Rust, based on the WHATWG URL Standard - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-0.6/default) >= 0.6.1
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust url crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
