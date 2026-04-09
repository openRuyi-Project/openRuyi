# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Encode
Version:        3.21
Release:        %autorelease
Summary:        Character encodings in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Encode
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DA/DANKOGAI/Encode-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More) >= 0.92

Requires:       perl(Exporter) >= 5.57
Requires:       perl(parent) >= 0.221

%description
The Encode module provides the interface between Perl strings and the rest
of the system. Perl strings are sequences of characters.

%prep
%setup -q -n Encode-%{version}

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
