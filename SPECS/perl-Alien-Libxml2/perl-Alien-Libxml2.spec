# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Alien-Libxml2
Version:        0.20
Release:        %autorelease
Summary:        Install the C libxml2 library on your system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-Libxml2
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-Libxml2-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Alien::Base) >= 2.37
BuildRequires:  perl(Alien::Build) >= 2.37
BuildRequires:  perl(Alien::Build::MM) >= 0.32
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(File::chdir)
# Manual
BuildRequires:  perl(Alien::Build::Plugin::Download::GitLab)
BuildRequires:  perl(URI)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Mozilla::CA)
BuildRequires:  libxml2-devel

Requires:       perl(Alien::Base) >= 2.37

%description
This module provides libxml2 for other modules to use.

%prep
%setup -q -n Alien-Libxml2-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc alienfile author.yml Changes perlcriticrc README

%changelog
%autochangelog
