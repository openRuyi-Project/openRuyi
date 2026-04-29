# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name http-auth
%global full_version 0.1.10
%global pkgname http-auth-0.1

Name:           rust-http-auth-0.1
Version:        0.1.10
Release:        %autorelease
Summary:        Rust crate "http-auth"
License:        MIT/Apache-2.0
URL:            https://github.com/scottlamb/http-auth
#!RemoteAsset:  sha256:150fa4a9462ef926824cf4519c84ed652ca8f4fbae34cb8af045b5cbcaf98822
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0/default) >= 2.8.0
Provides:       crate(%{pkgname})

%description
Likely to be extended with server support and additional auth schemes.
Source code for takopackized Rust crate "http-auth"

%package     -n %{name}+base64
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "base64" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(base64-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/base64)
Provides:       crate(%{pkgname}/basic-scheme)

%description -n %{name}+base64
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "base64" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "basic-scheme" feature.

%package     -n %{name}+default
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/basic-scheme)
Requires:       crate(%{pkgname}/digest-scheme)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "default" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "digest"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "digest" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest-scheme
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "digest-scheme"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/digest)
Requires:       crate(%{pkgname}/hex)
Requires:       crate(%{pkgname}/md-5)
Requires:       crate(%{pkgname}/rand)
Requires:       crate(%{pkgname}/sha2)
Provides:       crate(%{pkgname}/digest-scheme)

%description -n %{name}+digest-scheme
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "digest-scheme" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hex
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "hex"
Requires:       crate(%{pkgname})
Requires:       crate(hex-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/hex)

%description -n %{name}+hex
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "hex" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "http"
Requires:       crate(%{pkgname})
Requires:       crate(http-0.2/default) >= 0.2.5
Provides:       crate(%{pkgname}/http)

%description -n %{name}+http
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "http" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http10
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "http10"
Requires:       crate(%{pkgname})
Requires:       crate(http-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/http10)

%description -n %{name}+http10
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "http10" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "log" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/trace)

%description -n %{name}+log
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "log" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "trace" feature.

%package     -n %{name}+md-5
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "md-5"
Requires:       crate(%{pkgname})
Requires:       crate(md-5-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/md-5)

%description -n %{name}+md-5
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "md-5" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8/default) >= 0.8.4
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "rand" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Digest challenges - feature "sha2"
Requires:       crate(%{pkgname})
Requires:       crate(sha2-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/sha2)

%description -n %{name}+sha2
Likely to be extended with server support and additional auth schemes.
This metapackage enables feature "sha2" for the Rust http-auth crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
