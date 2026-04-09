# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-JSON-PP
Version:        4.16
Release:        %autorelease
Summary:        JSON::XS compatible pure-Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/JSON-PP
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/I/IS/ISHIGAKI/JSON-PP-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util) >= 1.08
BuildRequires:  perl(Test::More)

Requires:       perl(Scalar::Util) >= 1.08

%description
JSON::PP is a pure perl JSON decoder/encoder, and (almost) compatible to
much faster JSON::XS written by Marc Lehmann in C. JSON::PP works as a
fallback module when you use JSON module without having installed JSON::XS.

%prep
%setup -q -n JSON-PP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
