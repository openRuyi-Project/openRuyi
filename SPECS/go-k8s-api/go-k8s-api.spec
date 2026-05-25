# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  k8s.io/api

Name:           go-k8s-api
Version:        1.36.0~alpha2
Release:        %autorelease
Summary:        The canonical location of the Kubernetes API definition.
License:        Apache-2.0
URL:            https://github.com/kubernetes/api
#!RemoteAsset:  sha256:16b686cba723e99ae024d8dd896a2211ee3b7d4ed836c4de6b03bc54181a2296
Source0:        https://github.com/kubernetes/api/archive/refs/tags/kubernetes-1.36.0-alpha.2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n api-kubernetes-1.36.0-alpha.2

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/apitesting/fuzzer)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/apitesting/roundtrip)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/operation)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/safe)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/validate)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/validate/content)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/fuzzer)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  go(k8s.io/apimachinery/pkg/types)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/validation/field)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/klog/v2/ktesting)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(k8s.io/api) = %{version}
Provides:       go(k8s.io/api/admission/v1) = %{version}
Provides:       go(k8s.io/api/admission/v1beta1) = %{version}
Provides:       go(k8s.io/api/admissionregistration/v1) = %{version}
Provides:       go(k8s.io/api/admissionregistration/v1alpha1) = %{version}
Provides:       go(k8s.io/api/admissionregistration/v1beta1) = %{version}
Provides:       go(k8s.io/api/apidiscovery/v2) = %{version}
Provides:       go(k8s.io/api/apidiscovery/v2beta1) = %{version}
Provides:       go(k8s.io/api/apiserverinternal/v1alpha1) = %{version}
Provides:       go(k8s.io/api/apps/v1) = %{version}
Provides:       go(k8s.io/api/apps/v1beta1) = %{version}
Provides:       go(k8s.io/api/apps/v1beta2) = %{version}
Provides:       go(k8s.io/api/authentication/v1) = %{version}
Provides:       go(k8s.io/api/authentication/v1alpha1) = %{version}
Provides:       go(k8s.io/api/authentication/v1beta1) = %{version}
Provides:       go(k8s.io/api/authorization/v1) = %{version}
Provides:       go(k8s.io/api/authorization/v1beta1) = %{version}
Provides:       go(k8s.io/api/autoscaling/v1) = %{version}
Provides:       go(k8s.io/api/autoscaling/v2) = %{version}
Provides:       go(k8s.io/api/batch/v1) = %{version}
Provides:       go(k8s.io/api/batch/v1beta1) = %{version}
Provides:       go(k8s.io/api/certificates/v1) = %{version}
Provides:       go(k8s.io/api/certificates/v1alpha1) = %{version}
Provides:       go(k8s.io/api/certificates/v1beta1) = %{version}
Provides:       go(k8s.io/api/coordination/v1) = %{version}
Provides:       go(k8s.io/api/coordination/v1alpha2) = %{version}
Provides:       go(k8s.io/api/coordination/v1beta1) = %{version}
Provides:       go(k8s.io/api/core/v1) = %{version}
Provides:       go(k8s.io/api/discovery/v1) = %{version}
Provides:       go(k8s.io/api/discovery/v1beta1) = %{version}
Provides:       go(k8s.io/api/events/v1) = %{version}
Provides:       go(k8s.io/api/events/v1beta1) = %{version}
Provides:       go(k8s.io/api/extensions/v1beta1) = %{version}
Provides:       go(k8s.io/api/flowcontrol/v1) = %{version}
Provides:       go(k8s.io/api/flowcontrol/v1beta1) = %{version}
Provides:       go(k8s.io/api/flowcontrol/v1beta2) = %{version}
Provides:       go(k8s.io/api/flowcontrol/v1beta3) = %{version}
Provides:       go(k8s.io/api/imagepolicy/v1alpha1) = %{version}
Provides:       go(k8s.io/api/networking/v1) = %{version}
Provides:       go(k8s.io/api/networking/v1beta1) = %{version}
Provides:       go(k8s.io/api/node/v1) = %{version}
Provides:       go(k8s.io/api/node/v1alpha1) = %{version}
Provides:       go(k8s.io/api/node/v1beta1) = %{version}
Provides:       go(k8s.io/api/policy/v1) = %{version}
Provides:       go(k8s.io/api/policy/v1beta1) = %{version}
Provides:       go(k8s.io/api/rbac/v1) = %{version}
Provides:       go(k8s.io/api/rbac/v1alpha1) = %{version}
Provides:       go(k8s.io/api/rbac/v1beta1) = %{version}
Provides:       go(k8s.io/api/resource/v1) = %{version}
Provides:       go(k8s.io/api/resource/v1alpha3) = %{version}
Provides:       go(k8s.io/api/resource/v1beta1) = %{version}
Provides:       go(k8s.io/api/resource/v1beta2) = %{version}
Provides:       go(k8s.io/api/scheduling/v1) = %{version}
Provides:       go(k8s.io/api/scheduling/v1alpha1) = %{version}
Provides:       go(k8s.io/api/scheduling/v1beta1) = %{version}
Provides:       go(k8s.io/api/storage/v1) = %{version}
Provides:       go(k8s.io/api/storage/v1alpha1) = %{version}
Provides:       go(k8s.io/api/storage/v1beta1) = %{version}
Provides:       go(k8s.io/api/storagemigration/v1beta1) = %{version}

Requires:       go(github.com/fxamacker/cbor/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/x448/float16)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/inf.v0)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/apimachinery/pkg/api/equality)
Requires:       go(k8s.io/apimachinery/pkg/api/operation)
Requires:       go(k8s.io/apimachinery/pkg/api/resource)
Requires:       go(k8s.io/apimachinery/pkg/api/safe)
Requires:       go(k8s.io/apimachinery/pkg/api/validate)
Requires:       go(k8s.io/apimachinery/pkg/api/validate/content)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1)
Requires:       go(k8s.io/apimachinery/pkg/runtime)
Requires:       go(k8s.io/apimachinery/pkg/runtime/schema)
Requires:       go(k8s.io/apimachinery/pkg/types)
Requires:       go(k8s.io/apimachinery/pkg/util/intstr)
Requires:       go(k8s.io/apimachinery/pkg/util/validation)
Requires:       go(k8s.io/apimachinery/pkg/util/validation/field)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)


%description
| ⚠️ **This is an automatically published **staged repository
 | (https://git.k8s.io/kubernetes/staging#external-repository-staging-
 | area)**
 | for Kubernetes**. Contributions, including issues and pull requests,
 | should be made to the main Kubernetes repository:
 | https://github.com/kubernetes/kubernetes
 | (https://github.com/kubernetes/kubernetes). This repository is read-
 | only
 | for importing, and not used for direct contributions. See
 | CONTRIBUTING.md (/CONTRIBUTING.md) for more details.


%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
