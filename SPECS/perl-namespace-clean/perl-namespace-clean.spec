# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-namespace-clean
Version:        0.27
Release:        %autorelease
Summary:        Keep imports and functions out of your namespace
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/namespace-clean
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RI/RIBASUSHI/namespace-clean-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Package::Stash) >= 0.23
BuildRequires:  perl(Test::More) >= 0.47

Requires:       perl(B::Hooks::EndOfScope) >= 0.12
Requires:       perl(Package::Stash) >= 0.23

%description
Keeping packages clean

%prep
%setup -q -n namespace-clean-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
