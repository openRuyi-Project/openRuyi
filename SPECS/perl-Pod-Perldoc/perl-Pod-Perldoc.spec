# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Pod-Perldoc
Version:        3.28
Release:        %autorelease
Summary:        Look up Perl documentation in Pod format
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Pod-Perldoc
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/M/MA/MALLEN/Pod-Perldoc-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Man) >= 2.18
BuildRequires:  perl(Pod::Simple::RTF) >= 3.16
BuildRequires:  perl(Pod::Simple::XMLOutStream) >= 3.16
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)

Requires:       perl(File::Temp) >= 0.22
Requires:       perl(Pod::Man) >= 2.18
Requires:       perl(Pod::Simple::RTF) >= 3.16
Requires:       perl(Pod::Simple::XMLOutStream) >= 3.16

%description
perldoc looks up a piece of documentation in POD format that is embedded
in the perl installation tree or in a Perl script, and displays it via
"groff -man | $PAGER". This is primarily used for the documentation for
the Perl library modules.

%prep
%setup -q -n Pod-Perldoc-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes perldoc README

%changelog
%autochangelog
