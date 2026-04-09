# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-HomeDir
Version:        1.006
Release:        %autorelease
Summary:        Find your home and other directories on any platform
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-HomeDir
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RE/REHSACK/File-HomeDir-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.3
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd) >= 3
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.01
BuildRequires:  perl(File::Spec) >= 3
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(File::Which) >= 0.05
# Bruh we are on Linux
#BuildRequires:  perl(Mac::SystemDirectory) >= 0.04
BuildRequires:  perl(Test::More) >= 0.9

Requires:       perl(Cwd) >= 3.12
Requires:       perl(File::Path) >= 2.01
Requires:       perl(File::Spec) >= 3.12
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(File::Which) >= 0.05

%description
File::HomeDir is a module for locating the directories that are "owned" by
a user (typically your user) and to solve the various issues that arise
trying to find them consistently across a wide variety of platforms.

%prep
%setup -q -n File-HomeDir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md

%changelog
%autochangelog
