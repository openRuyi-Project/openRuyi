# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-HTTP-Response-Encoding
Version:        0.06
Release:        %autorelease
Summary:        HTTP::Response::Encoding Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTTP-Response-Encoding
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DA/DANKOGAI/HTTP-Response-Encoding-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Encode) >= 2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Test::More)

Requires:       perl(Encode) >= 2

%description
SYNOPSIS      use LWP::UserAgent;      use HTTP::Response::Encoding;

%prep
%setup -q -n HTTP-Response-Encoding-%{version}

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
