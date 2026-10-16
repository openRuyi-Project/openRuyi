# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ossl
%global full_version 1.5.3
%global pkgname ossl-1

Name:           rust-ossl-1
Version:        1.5.3
Release:        %autorelease
Summary:        Rust crate "ossl"
License:        Apache-2.0
URL:            https://github.com/latchset/kryoptic
#!RemoteAsset:  sha256:4fa44e30f9538a8ff3c06349a4206f62f3e68c8d47aaeec0d6d63b1e044fd537
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bindgen-0.72) >= 0.72.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.151
Requires:       crate(pkg-config-0.3) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/ossl320) = %{version}
Provides:       crate(%{pkgname}/ossl350) = %{version}
Provides:       crate(%{pkgname}/ossl400) = %{version}
Provides:       crate(%{pkgname}/rfc9580) = %{version}

%description
Source code for takopackized Rust crate "ossl"

%package     -n %{name}+dynamic
Summary:        OpenSSL version 3+ bindings to modern EVP APIs - feature "dynamic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ossl-sys-1/dynamic) >= 1.5.3
Provides:       crate(%{pkgname}/dynamic) = %{version}

%description -n %{name}+dynamic
This metapackage enables feature "dynamic" for the Rust ossl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        OpenSSL version 3+ bindings to modern EVP APIs - feature "fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ossl400) = %{version}
Requires:       crate(ossl-sys-1/fips) >= 1.5.3
Provides:       crate(%{pkgname}/fips) = %{version}

%description -n %{name}+fips
This metapackage enables feature "fips" for the Rust ossl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        OpenSSL version 3+ bindings to modern EVP APIs - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/std) >= 0.4.27
Requires:       crate(vsprintf-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust ossl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl-sys
Summary:        OpenSSL version 3+ bindings to modern EVP APIs - feature "openssl-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-sys-0.9/bindgen) >= 0.9.0
Requires:       crate(openssl-sys-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/openssl-sys) = %{version}

%description -n %{name}+openssl-sys
This metapackage enables feature "openssl-sys" for the Rust ossl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ossl-sys
Summary:        OpenSSL version 3+ bindings to modern EVP APIs - feature "ossl-sys" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ossl-sys-1/default) >= 1.5.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/ossl-sys) = %{version}

%description -n %{name}+ossl-sys
This metapackage enables feature "ossl-sys" for the Rust ossl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
