# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-File-ShareDir
Version:        1.001002
Release:        %autorelease
Summary:        Create a Fake ShareDir for your modules for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-File-ShareDir
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/K/KE/KENTNL/Test-File-ShareDir-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny) >= 0.018
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)

Requires:       perl(Exporter) >= 5.57
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(Path::Tiny) >= 0.018

%description
Test::File::ShareDir is some low level plumbing to enable a distribution to
perform tests while consuming its own share directories in a manner similar
to how they will be once installed.

%prep
%setup -q -n Test-File-ShareDir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes dist.ini.meta perlcritic.rc README weaver.ini

%changelog
%autochangelog
