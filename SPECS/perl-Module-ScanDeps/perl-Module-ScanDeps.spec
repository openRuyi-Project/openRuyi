# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-ScanDeps
Version:        1.37
Release:        %autorelease
Summary:        Recursively scan Perl code for dependencies
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-ScanDeps
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RS/RSCHUPP/Module-ScanDeps-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.9
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Run3) >= 0.048
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(version)

Requires:       perl(List::Util) >= 1.33

%description
This module scans potential modules used by perl programs, and returns a
hash reference; its keys are the module names as appears in %INC (e.g.
Test/More.pm); the values are hash references with this structure:

%prep
%setup -q -n Module-ScanDeps-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc AUTHORS Changes README

%changelog
%autochangelog
