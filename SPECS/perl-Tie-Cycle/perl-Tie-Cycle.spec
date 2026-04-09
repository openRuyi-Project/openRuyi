# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Tie-Cycle
Version:        1.231
Release:        %autorelease
Summary:        Cycle through a list of values via a scalar
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Tie-Cycle
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BR/BRIANDFOY/Tie-Cycle-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(version) >= 0.86

%description
You use Tie::Cycle to go through a list over and over again. Once you get
to the end of the list, you go back to the beginning. You don't have to
worry about any of this since the magic of tie does that for you.

%prep
%setup -q -n Tie-Cycle-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md INSTALL.SKIP SECURITY.md

%changelog
%autochangelog
