# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DateTime-TimeZone-SystemV
Version:        0.010
Release:        %autorelease
Summary:        System V and POSIX timezone strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DateTime-TimeZone-SystemV
#!RemoteAsset:  sha256:827bce3c45c2777331cba201e31801945aeeb18c59aed3d94c2b2adb209d954a
Source0:        https://www.cpan.org/authors/id/Z/ZE/ZEFRAM/DateTime-TimeZone-SystemV-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::ISO8601)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
An instance of this class represents a timezone that was specified by means
of a System V timezone recipe or an extended form of the same syntax (such
as that specified by POSIX). These can express a plain offset from
Universal Time, or a system of two offsets (standard and daylight saving
time) switching on a yearly cycle according to certain types of rule.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
