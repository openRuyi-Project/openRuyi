# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-ShareDir
Version:        1.118
Release:        %autorelease
Summary:        Locate per-dist and per-module shared files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-ShareDir
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RE/REHSACK/File-ShareDir-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inspector) >= 1.12
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::ShareDir::Install) >= 0.13
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(List::MoreUtils) >= 0.428
BuildRequires:  perl(Params::Util) >= 1.07
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(warnings)

Requires:       perl(Class::Inspector) >= 1.12
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(List::MoreUtils) >= 0.428
Requires:       perl(Params::Util) >= 1.07

%description
The intent of File::ShareDir is to provide a companion to Class::Inspector
and File::HomeDir, modules that take a process that is well-known by
advanced Perl developers but gets a little tricky, and make it more
available to the larger Perl community.

%prep
%setup -q -n File-ShareDir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md testrules.yml

%changelog
%autochangelog
