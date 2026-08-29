# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cookie
%global full_version 0.18.1
%global pkgname cookie-0.18

Name:           rust-cookie-0.18
Version:        0.18.1
Release:        %autorelease
Summary:        Rust crate "cookie"
License:        MIT OR Apache-2.0
URL:            https://github.com/SergioBenitez/cookie-rs
#!RemoteAsset:  sha256:4ddef33a339a91ea89fb53151bd0a4689cfce27055c291dfa69945475d22c747
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(time-0.3/formatting) >= 0.3.0
Requires:       crate(time-0.3/macros) >= 0.3.0
Requires:       crate(time-0.3/parsing) >= 0.3.0
Requires:       crate(time-0.3/std) >= 0.3.0
Requires:       crate(version-check-0.9) >= 0.9.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Supports signed and private (encrypted, authenticated) jars.
Source code for takopackized Rust crate "cookie"

%package     -n %{name}+aes-gcm
Summary:        HTTP cookie parsing and cookie jar management - feature "aes-gcm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-gcm-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/aes-gcm) = %{version}

%description -n %{name}+aes-gcm
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "aes-gcm" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        HTTP cookie parsing and cookie jar management - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "base64" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hkdf
Summary:        HTTP cookie parsing and cookie jar management - feature "hkdf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hkdf-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/hkdf) = %{version}

%description -n %{name}+hkdf
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "hkdf" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hmac
Summary:        HTTP cookie parsing and cookie jar management - feature "hmac"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hmac-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/hmac) = %{version}

%description -n %{name}+hmac
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "hmac" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+key-expansion
Summary:        HTTP cookie parsing and cookie jar management - feature "key-expansion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hkdf) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/key-expansion) = %{version}

%description -n %{name}+key-expansion
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "key-expansion" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+percent-encoding
Summary:        HTTP cookie parsing and cookie jar management - feature "percent-encoding" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(percent-encoding-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/percent-encode) = %{version}
Provides:       crate(%{pkgname}/percent-encoding) = %{version}

%description -n %{name}+percent-encoding
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "percent-encoding" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "percent-encode" feature.

%package     -n %{name}+private
Summary:        HTTP cookie parsing and cookie jar management - feature "private"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aes-gcm) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/subtle) = %{version}
Provides:       crate(%{pkgname}/private) = %{version}

%description -n %{name}+private
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "private" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        HTTP cookie parsing and cookie jar management - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "rand" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+secure
Summary:        HTTP cookie parsing and cookie jar management - feature "secure"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/key-expansion) = %{version}
Requires:       crate(%{pkgname}/private) = %{version}
Requires:       crate(%{pkgname}/signed) = %{version}
Provides:       crate(%{pkgname}/secure) = %{version}

%description -n %{name}+secure
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "secure" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        HTTP cookie parsing and cookie jar management - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "sha2" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signed
Summary:        HTTP cookie parsing and cookie jar management - feature "signed"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/hmac) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Requires:       crate(%{pkgname}/subtle) = %{version}
Provides:       crate(%{pkgname}/signed) = %{version}

%description -n %{name}+signed
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "signed" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        HTTP cookie parsing and cookie jar management - feature "subtle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(subtle-2/default) >= 2.3.0
Provides:       crate(%{pkgname}/subtle) = %{version}

%description -n %{name}+subtle
Supports signed and private (encrypted, authenticated) jars.
This metapackage enables feature "subtle" for the Rust cookie crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
