# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Install
Version:        1.21
Release:        %autorelease
Summary:        Standalone, extensible Perl module installer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Install
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/Module-Install-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Archive::Zip) >= 1.37
BuildRequires:  perl(autodie)
BuildRequires:  perl(Devel::PPPort) >= 3.16
BuildRequires:  perl(ExtUtils::Install) >= 1.52
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.19
BuildRequires:  perl(File::HomeDir) >= 1
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Remove) >= 1.42
BuildRequires:  perl(File::Spec) >= 3.28
BuildRequires:  perl(JSON) >= 2.9
BuildRequires:  perl(LWP::Simple) >= 6.00
BuildRequires:  perl(LWP::UserAgent) >= 6.05
BuildRequires:  perl(Module::Build) >= 0.29
BuildRequires:  perl(Module::CoreList) >= 2.17
BuildRequires:  perl(Module::ScanDeps) >= 1.09
BuildRequires:  perl(PAR::Dist) >= 0.29
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.4413
BuildRequires:  perl(Test::Harness) >= 3.13
BuildRequires:  perl(Test::More) >= 0.86
BuildRequires:  perl(YAML::Tiny) >= 1.38

Requires:       perl(Archive::Zip) >= 1.37
Requires:       perl(Devel::PPPort) >= 3.16
Requires:       perl(ExtUtils::Install) >= 1.52
Requires:       perl(ExtUtils::MakeMaker) >= 6.59
Requires:       perl(ExtUtils::ParseXS) >= 2.19
Requires:       perl(File::HomeDir) >= 1
Requires:       perl(File::Remove) >= 1.42
Requires:       perl(File::Spec) >= 3.28
Requires:       perl(JSON) >= 2.9
Requires:       perl(LWP::Simple) >= 6.00
Requires:       perl(LWP::UserAgent) >= 6.05
Requires:       perl(Module::Build) >= 0.29
Requires:       perl(Module::CoreList) >= 2.17
Requires:       perl(Module::ScanDeps) >= 1.09
Requires:       perl(PAR::Dist) >= 0.29
Requires:       perl(Parse::CPAN::Meta) >= 1.4413
Requires:       perl(YAML::Tiny) >= 1.38

%description
Module::Install is a package for writing installers for CPAN (or CPAN-like)
distributions that are clean, simple, minimalist, act in a strictly correct
manner with ExtUtils::MakeMaker, and will run on any Perl installation
version 5.005 or newer.

%prep
%setup -q -n Module-Install-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TODO

%changelog
%autochangelog
