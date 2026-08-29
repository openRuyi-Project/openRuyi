# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-MIME-Base64
Version:        3.16
Release:        %autorelease
Summary:        Encoding and decoding of base64 strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MIME-Base64
#!RemoteAsset:  sha256:77f73d6f7aeb8d33be08b0d8c2617f9b6c77fb7fc45422d507ca8bafe4246017
Source0:        https://www.cpan.org/authors/id/C/CA/CAPOEIRAB/MIME-Base64-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-devel

%description
This module provides functions to encode and decode strings into and from
the base64 encoding specified in RFC 2045 - MIME (Multipurpose Internet
Mail Extensions). The base64 encoding is designed to represent arbitrary
sequences of octets in a form that need not be humanly readable. A 65-
character subset ([A-Za-z0-9+/=]) of US-ASCII is used, enabling 6 bits to
be represented per printable character.

%files -f %{name}.files
%doc benchmark benchmark-qp Changes README

%changelog
%autochangelog
