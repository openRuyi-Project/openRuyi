# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-Soundex
Version:        3.05
Release:        %autorelease
Summary:        Implementation of the soundex algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-Soundex
#!RemoteAsset:  sha256:f6dd55b4280b25dea978221839864382560074e1d6933395faee2510c2db60ed
Source0:        https://www.cpan.org/authors/id/R/RJ/RJBS/Text-Soundex-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(if)
BuildRequires:  perl-devel

%description
Soundex is a phonetic algorithm for indexing names by sound, as pronounced
in English. The goal is for names with the same pronunciation to be encoded
to the same representation so that they can be matched despite minor
differences in spelling. Soundex is the most widely known of all phonetic
algorithms and is often used (incorrectly) as a synonym for "phonetic
algorithm". Improvements to Soundex are the basis for many modern phonetic
algorithms. (Wikipedia, 2007)

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
