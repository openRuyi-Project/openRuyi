# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Perl-MinimumVersion
Version:        1.44
Release:        %autorelease
Summary:        Find a minimum required version of perl for Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Perl-MinimumVersion
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DB/DBOOK/Perl-MinimumVersion-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util) >= 1.20
BuildRequires:  perl(Params::Util) >= 0.25
BuildRequires:  perl(PPI) >= 1.252
BuildRequires:  perl(PPI::Util)
BuildRequires:  perl(PPIx::Regexp) >= 0.051
BuildRequires:  perl(PPIx::Utils)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(vars)
BuildRequires:  perl(version) >= 0.76
BuildRequires:  perl(warnings)

Requires:       perl(List::Util) >= 1.20
Requires:       perl(Params::Util) >= 0.25
Requires:       perl(PPI) >= 1.252
Requires:       perl(PPIx::Regexp) >= 0.051
Requires:       perl(version) >= 0.76

%description
Perl::MinimumVersion takes Perl source code and calculates the minimum
version of perl required to be able to run it. Because it is based on PPI,
it can do this without having to actually load the code.

%prep
%setup -q -n Perl-MinimumVersion-%{version}

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
