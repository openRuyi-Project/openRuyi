# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sscg
Version:        4.0.3
Release:        %autorelease
Summary:        Simple Signed Certificate Generator
License:        GPL-3.0-or-later WITH cryptsetup-OpenSSL-exception
URL:            https://github.com/sgallagher/sscg
#!RemoteAsset
Source0:        https://github.com/sgallagher/sscg/archive/refs/tags/sscg-%{version}.tar.gz
BuildSystem:    meson

BuildOption(prep):  -n %{name}-%{name}-%{version} -p1

BuildRequires:  gcc
BuildRequires:  openssl
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  meson
BuildRequires:  help2man

%description
SSCG(Simple Signed Certificate Generator) makes it easy to generate usable and secure
"self-signed" certificates. The certificates created by this tool are generated in a way
so as to create a CA certificate that can be safely imported into a client machine to trust
the service certificate without needing to set up a full PKI environment and without exposing
the machine to a risk of false signatures from the service certificate.

%files
%license COPYING
%doc README.md
%{_bindir}/sscg
%{_mandir}/man8/sscg.8*

%changelog
%autochangelog
