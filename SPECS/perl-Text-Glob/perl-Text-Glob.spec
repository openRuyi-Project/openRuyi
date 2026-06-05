# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-Glob
Version:        0.11
Release:        %autorelease
Summary:        Match globbing patterns against text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Text-Glob
#!RemoteAsset:  sha256:069ccd49d3f0a2dedb115f4bdc9fbac07a83592840953d1fcdfc39eb9d305287
Source0:        https://www.cpan.org/authors/id/R/RC/RCLAMP/Text-Glob-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.5.0
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
Text::Glob implements glob(3) style matching that can be used to match
against text, rather than fetching names from a filesystem. If you want to
do full file globbing use the File::Glob module instead.

%files -f %{name}.files
%doc Changes

%changelog
%autochangelog
