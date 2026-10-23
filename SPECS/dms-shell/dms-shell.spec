# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dms
%define go_import_path  github.com/AvengeMedia/DankMaterialShell/core

Name:           dms-shell
Version:        1.4.6
Release:        %autorelease
Summary:        Dank Material Shell for Quickshell
License:        MIT AND Apache-2.0 AND OFL-1.1 AND CC-BY-SA-4.0 AND CC-BY-3.0 AND GPL-2.0-or-later AND GPL-3.0-only
URL:            https://danklinux.com/docs/dankmaterialshell/overview
VCS:            git:https://github.com/AvengeMedia/DankMaterialShell.git
#!RemoteAsset:  sha256:f9db8badb2aea0d02b715743b678fc1386bb68266cb40d7846b05919ca975c03
Source0:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-cli-%{version}.tar.gz
#!RemoteAsset:  sha256:0575156bf6610165c983e38b9481a29cd8a51261145b4f0220dc9daabebc8625
Source1:        https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%{version}/dms-qml.tar.gz#/dms-qml-%{version}.tar.gz
BuildSystem:    golang

# Test the distribution command variant used by the packaged executable.
BuildOption(check):  -tags=distro_binary

BuildRequires:  bash-completion
BuildRequires:  desktop-file-utils
BuildRequires:  go >= 1.25.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Wifx/gonetworkmanager/v2)
BuildRequires:  go(github.com/alecthomas/chroma/v2)
BuildRequires:  go(github.com/charmbracelet/bubbles)
BuildRequires:  go(github.com/charmbracelet/bubbletea)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/charmbracelet/log)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-git/go-git/v6)
BuildRequires:  go(github.com/godbus/dbus/v5)
BuildRequires:  go(github.com/holoplot/go-evdev)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/pilebones/go-udev)
BuildRequires:  go(github.com/sblinch/kdl-go)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/yuin/goldmark)
BuildRequires:  go(github.com/yuin/goldmark-highlighting/v2)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  systemd-rpm-macros

Requires:       dms-cli = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       quickshell

%description
Dank Material Shell is a Material Design shell for Wayland compositors,
built with Quickshell and a Go backend.

%package     -n dms-cli
Summary:        CLI and backend for Dank Material Shell
Provides:       dms = %{version}-%{release}

%description -n dms-cli
The dms-cli package provides the dms command line interface, backend,
and shell completions used by Dank Material Shell.

%prep
%autosetup -n dms-cli-%{version}
# Remove vendored dependencies before copying the sources into GOPATH.
rm -rf vendor
%go_prep
mkdir dms-qml
tar -xzf %{SOURCE1} -C dms-qml

%build
%go_common
dms_build_dir="$PWD"
export CGO_ENABLED=0
export GOCACHE=%{_builddir}/go-build-cache
export GOTOOLCHAIN=local
cd %{_builddir}/go/src/%{go_import_path}
%__go build -v -trimpath -buildvcs=false -tags distro_binary \
    -ldflags "-s -w -X main.Version=%{version}" -o "$dms_build_dir/dms" ./cmd/dms

%install -a
install -dm0755 %{buildroot}%{bash_completions_dir}
install -dm0755 %{buildroot}%{_datadir}/fish/vendor_completions.d
install -dm0755 %{buildroot}%{_datadir}/zsh/site-functions
%{buildroot}%{_bindir}/dms completion bash > %{buildroot}%{bash_completions_dir}/dms
%{buildroot}%{_bindir}/dms completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/dms.fish
%{buildroot}%{_bindir}/dms completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_dms

install -dm0755 %{buildroot}%{_datadir}/quickshell/dms
cp -a dms-qml/. %{buildroot}%{_datadir}/quickshell/dms/

install -Dm0644 dms-qml/assets/systemd/dms.service %{buildroot}%{_userunitdir}/dms.service
install -Dm0644 dms-qml/assets/dms-open.desktop %{buildroot}%{_datadir}/applications/dms-open.desktop
install -Dm0644 dms-qml/assets/danklogo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/danklogo.svg

%check -a
%{buildroot}%{_bindir}/dms --help >/dev/null
%{buildroot}%{_bindir}/dms completion bash >/dev/null
test -f %{buildroot}%{_datadir}/quickshell/dms/shell.qml
test -f %{buildroot}%{_datadir}/quickshell/dms/VERSION
desktop-file-validate %{buildroot}%{_datadir}/applications/dms-open.desktop

%post
%systemd_user_post dms.service

%preun
%systemd_user_preun dms.service

%postun
%systemd_user_postun_with_reload dms.service

%files
%doc dms-qml/README.md
%license dms-qml/LICENSE
%license dms-qml/assets/fonts/inter/LICENSE.txt
%license dms-qml/assets/fonts/material-design-icons/LICENSE
%license dms-qml/assets/fonts/nerd-fonts/LICENSE
%license dms-qml/assets/sounds/freedesktop/CREDITS
%license dms-qml/assets/sounds/plasma/LICENSE
%{_datadir}/applications/dms-open.desktop
%{_datadir}/icons/hicolor/scalable/apps/danklogo.svg
%{_datadir}/quickshell/dms/
%{_userunitdir}/dms.service

%files -n dms-cli
%doc README.md
%license dms-qml/LICENSE
%license pkg/go-wayland/LICENSE
%license pkg/ipp/LICENSE
%license pkg/syncmap/LICENSE
%{_bindir}/dms
%{bash_completions_dir}/dms
%{_datadir}/fish/vendor_completions.d/dms.fish
%{_datadir}/zsh/site-functions/_dms

%changelog
%autochangelog
