# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Pod-Parser
Version:        1.67
Release:        %autorelease
Summary:        Base class for creating POD filters and translators
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Pod-Parser
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/M/MA/MAREKR/Pod-Parser-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Test::More) >= 0.6

Requires:       perl(Test::More) >= 0.6

%description
NOTE: This module is considered legacy; modern Perl releases (5.31.1 and
      higher) are going to remove Pod-Parser from core and use Pod::Simple
      for all things POD.

%prep
%setup -q -n Pod-Parser-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ANNOUNCE CHANGES README TODO

%changelog
%autochangelog
