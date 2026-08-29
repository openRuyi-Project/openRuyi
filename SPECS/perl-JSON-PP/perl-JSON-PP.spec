# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-JSON-PP
Version:        4.18
Release:        %autorelease
Summary:        JSON::XS compatible pure-Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/JSON-PP
#!RemoteAsset:  sha256:9c7bcb238183c4240db5548b1910ce8428e0464d05e413df5893998e67bf602c
Source0:        https://www.cpan.org/authors/id/I/IS/ISHIGAKI/JSON-PP-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util) >= 1.08
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(Scalar::Util) >= 1.08
Requires:       perl(Test::More) >= 0.88

%description
JSON::PP is a pure perl JSON decoder/encoder, and (almost) compatible to
much faster JSON::XS written by Marc Lehmann in C. JSON::PP works as a
fallback module when you use JSON module without having installed JSON::XS.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
