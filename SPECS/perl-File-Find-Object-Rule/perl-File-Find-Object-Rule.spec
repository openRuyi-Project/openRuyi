# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-File-Find-Object-Rule
Version:        0.0313
Release:        %autorelease
Summary:        Alternative interface to File::Find::Object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-Find-Object-Rule
#!RemoteAsset:  sha256:81940f299d6487248fbf30d8f1fb7df6c6a34b3df9440a5621b135c8e34fcff2
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Find-Object-Rule-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find::Object)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::TreeCreate)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Number::Compare)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Glob)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
File::Find::Object::Rule is a friendlier interface to File::Find::Object .
It allows you to build rules which specify the desired files and
directories.

%prep
%setup -q -n File-Find-Object-Rule-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --installdirs=vendor --destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Changes.F-F-R README weaver.ini
%license LICENSE

%changelog
%autochangelog
