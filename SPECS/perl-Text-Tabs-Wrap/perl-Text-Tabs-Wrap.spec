# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Text-Tabs-Wrap
Version:        2024.001
Release:        %autorelease
Summary:        Expand tabs and do simple line wrapping
License:        TTWL
URL:            https://metacpan.org/release/Text-Tabs%2BWrap
#!RemoteAsset:  sha256:fa83812ad59b111c543a3678115012aeb3e4ab3067c2261a38fdbcacf1b761cd
Source0:        https://www.cpan.org/authors/id/A/AR/ARISTOTLE/Text-Tabs+Wrap-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(re)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(bytes)

%description
Text::Tabs performs the same job that the UNIX expand(1) and unexpand(1)
commands do: adding or removing tabs from a document.

Text::Wrap::wrap() will reformat lines into paragraphs. All it does is break
up long lines, it will not join short lines together.

%files -f %{name}.files
%doc README

%changelog
%autochangelog
