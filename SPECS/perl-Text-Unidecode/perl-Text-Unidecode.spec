# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-Unidecode
Version:        1.30
Release:        %autorelease
Summary:        Plain ASCII transliterations of Unicode text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-Unidecode
#!RemoteAsset:  sha256:6c24f14ddc1d20e26161c207b73ca184eed2ef57f08b5fb2ee196e6e2e88b1c6
Source0:        https://www.cpan.org/authors/id/S/SB/SBURKE/Text-Unidecode-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
It often happens that you have non-Roman text data in Unicode, but you
can't display it-- usually because you're trying to show it to a user via
an application that doesn't support Unicode, or because the fonts you need
aren't accessible. You could represent the Unicode characters as "???????"
or "\15BA\15A0\1610...", but that's nearly useless to the user who actually
wants to read what the text says.

%files -f %{name}.files
%doc ChangeLog README TODO.txt

%changelog
%autochangelog
