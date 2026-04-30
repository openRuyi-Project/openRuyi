# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Dir-Manifest
Version:        0.6.1
Release:        %autorelease
Summary:        Treat a directory and a manifest file as a hash/dictionary of keys to texts or blobs
License:        MIT
URL:            https://metacpan.org/dist/Dir-Manifest
#!RemoteAsset:  sha256:84ff7226873d5e8656ec77344c0838c153a9f015b46b60e1fe8798bb2927e505
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Dir-Manifest-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Here is the primary use case: you have several long texts (and/or binary
blobs) that you wish to load from the code (e.g: for the "want"/expected
values of tests) and you wish to conventiently edit them, track them and
maintain them. Using Dir::Manifest you can put each in a separate file in a
directory, create a manifest file listing all valid filenames/key and then
say something like my $text = $dir->text("deal24solution.txt", {lf => 1}).
And hopefully it will be done securely and reliably.

%prep
%setup -q -n Dir-Manifest-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot}
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README README.mkdn weaver.ini
%license LICENSE

%changelog
%autochangelog
