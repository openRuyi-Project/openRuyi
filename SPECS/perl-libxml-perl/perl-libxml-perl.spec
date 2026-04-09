# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-libxml-perl
Version:        0.08
Release:        %autorelease
Summary:        libxml::perl Perl module
License:        CHECK(GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/dist/libxml-perl
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/K/KM/KMACLEOD/libxml-perl-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(XML::Parser) >= 2.19

%description
libxml-perl is a collection of smaller Perl modules, scripts, and documents
for working with XML in Perl.  libxml-perl software works in combination
with XML::Parser, PerlSAX, XML::DOM, XML::Grove and others.

%prep
%setup -q -n libxml-perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog Changes libxml-perl-0.08.spec libxml-perl.spec README

%changelog
%autochangelog
