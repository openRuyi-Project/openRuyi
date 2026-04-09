# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Pod-Usage
Version:        2.05
Release:        %autorelease
Summary:        Extracts POD documentation and shows usage information
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Pod-Usage
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/M/MA/MAREKR/Pod-Usage-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Pod::Perldoc) >= 3.28
BuildRequires:  perl(Pod::Simple) >= 3.40
BuildRequires:  perl(Pod::Text) >= 4.00
BuildRequires:  perl(Test::More) >= 0.60

Requires:       perl(File::Spec) >= 0.82
Requires:       perl(Pod::Perldoc) >= 3.28
Requires:       perl(Pod::Simple) >= 3.40
Requires:       perl(Pod::Text) >= 4.00

%description
pod2usage will print a usage message for the invoking script (using its
embedded POD documentation) and then exit the script with the desired exit
status.

%prep
%setup -q -n Pod-Usage-%{version}

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
