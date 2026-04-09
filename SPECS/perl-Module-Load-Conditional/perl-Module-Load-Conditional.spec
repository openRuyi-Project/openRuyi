# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Load-Conditional
Version:        0.74
Release:        %autorelease
Summary:        Looking up module information / loading at runtime
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Load-Conditional
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Module-Load-Conditional-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::CoreList) >= 2.22
BuildRequires:  perl(Module::Load) >= 0.28
BuildRequires:  perl(Module::Metadata) >= 1.000005
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version) >= 0.69

Requires:       perl(Module::CoreList) >= 2.22
Requires:       perl(Module::Load) >= 0.28
Requires:       perl(Module::Metadata) >= 1.000005
Requires:       perl(version) >= 0.69

%description
Module::Load::Conditional provides simple ways to query and possibly load
any of the modules you have installed on your system during runtime.

%prep
%setup -q -n Module-Load-Conditional-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES README

%changelog
%autochangelog
