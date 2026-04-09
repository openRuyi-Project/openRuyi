# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-ExtUtils-Install
Version:        2.22
Release:        %autorelease
Summary:        Install files from here to there
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-Install
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/ExtUtils-Install-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.47

Requires:       perl(Test::More) >= 0.47

%description
Handles the installing and uninstalling of perl modules, scripts, man
pages, etc...

%prep
%setup -q -n ExtUtils-Install-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes INSTALL.SKIP README

%changelog
%autochangelog
