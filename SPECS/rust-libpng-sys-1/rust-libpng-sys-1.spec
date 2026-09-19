# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libpng-sys
%global full_version 1.1.11
%global pkgname libpng-sys-1

Name:           rust-libpng-sys-1
Version:        1.1.11
Release:        %autorelease
Summary:        Rust crate "libpng-sys"
License:        Libpng
URL:            http://www.libpng.org/pub/png/libpng.html
#!RemoteAsset:  sha256:2e8d56e0541e2b1d73868e7b877624e1f9ce8787a91acdb867c30c579349d38b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.1.20
Requires:       crate(dunce-1) >= 1.0.5
Requires:       crate(libc-0.2/default) >= 0.2.158
Requires:       crate(pkg-config-0.3) >= 0.3.30

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/build) = %{version}
Provides:       crate(%{pkgname}/static) = %{version}

%description
They're likely to bring sorrow and regret. Please use a native Rust PNG library instead.
Source code for takopackized Rust crate "libpng-sys"

%package     -n %{name}+cloudflare-zlib-sys
Summary:        Unreliable bindings for libpng 1.6 - feature "cloudflare-zlib-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cloudflare-zlib-sys-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname}/cloudflare-zlib-sys) = %{version}

%description -n %{name}+cloudflare-zlib-sys
They're likely to bring sorrow and regret. Please use a native Rust PNG library instead.
This metapackage enables feature "cloudflare-zlib-sys" for the Rust libpng-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libz-sys
Summary:        Unreliable bindings for libpng 1.6 - feature "libz-sys" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libz-sys-1/default) >= 1.1.20
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/libz-sys) = %{version}

%description -n %{name}+libz-sys
They're likely to bring sorrow and regret. Please use a native Rust PNG library instead.
This metapackage enables feature "libz-sys" for the Rust libpng-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+static-libz
Summary:        Unreliable bindings for libpng 1.6 - feature "static-libz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libz-sys-1/static) >= 1.1.20
Provides:       crate(%{pkgname}/static-libz) = %{version}

%description -n %{name}+static-libz
They're likely to bring sorrow and regret. Please use a native Rust PNG library instead.
This metapackage enables feature "static-libz" for the Rust libpng-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
