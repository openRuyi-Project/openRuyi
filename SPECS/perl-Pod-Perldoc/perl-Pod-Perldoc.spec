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
#!RemoteAsset:  sha256:cc41e605b8e13c40a8ee6504ff46347b5ba7fbd92203b3bb055422051befc64d
Source0:        https://www.cpan.org/authors/id/M/MA/MALLEN/Pod-Perldoc-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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
The guts of perldoc utility.

%files -f %{name}.files
%doc Changes perldoc README

%changelog
%autochangelog
