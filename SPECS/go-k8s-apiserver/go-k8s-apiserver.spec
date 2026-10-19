# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           apiserver
%define go_import_path  k8s.io/apiserver

Name:           go-k8s-apiserver
Version:        0.36.2
Release:        %autorelease
Summary:        Kubernetes API server library
License:        Apache-2.0
URL:            https://github.com/kubernetes/apiserver
#!RemoteAsset:  sha256:8a6cba51a468271854ddda86895f121a050795c3c0c1fe3087d073c05d58e061
Source0:        https://github.com/kubernetes/apiserver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/blang/semver/v4)
BuildRequires:  go(github.com/coreos/go-oidc)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/google/cel-go)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/mxk/go-flowrate)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.etcd.io/etcd/api/v3)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(go.etcd.io/etcd/server/v3)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/attribute)
BuildRequires:  go(go.opentelemetry.io/otel/exporters)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/semconv/v1.12.0)
BuildRequires:  go(go.opentelemetry.io/otel/semconv/v1.17.0)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.uber.org/zap/zapcore)
BuildRequires:  go(go.uber.org/zap/zaptest)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/genproto/googleapis)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/credentials)
BuildRequires:  go(google.golang.org/grpc/grpclog)
BuildRequires:  go(google.golang.org/grpc/metadata)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)
BuildRequires:  go(google.golang.org/protobuf/types)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(gopkg.in/go-jose/go-jose.v2)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(k8s.io/api/admission/v1)
BuildRequires:  go(k8s.io/api/admission/v1beta1)
BuildRequires:  go(k8s.io/api/admissionregistration/v1)
BuildRequires:  go(k8s.io/api/apidiscovery/v2)
BuildRequires:  go(k8s.io/api/apidiscovery/v2beta1)
BuildRequires:  go(k8s.io/api/apiserverinternal/v1alpha1)
BuildRequires:  go(k8s.io/api/apps/v1)
BuildRequires:  go(k8s.io/api/authentication/v1)
BuildRequires:  go(k8s.io/api/authentication/v1beta1)
BuildRequires:  go(k8s.io/api/authorization/v1)
BuildRequires:  go(k8s.io/api/authorization/v1beta1)
BuildRequires:  go(k8s.io/api/batch/v1)
BuildRequires:  go(k8s.io/api/coordination/v1)
BuildRequires:  go(k8s.io/api/core/v1)
BuildRequires:  go(k8s.io/api/discovery/v1)
BuildRequires:  go(k8s.io/api/extensions/v1beta1)
BuildRequires:  go(k8s.io/api/flowcontrol/v1)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/apitesting)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/apitesting/fuzzer)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/apitesting/roundtrip)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/meta)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/operation)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/validate/content)
BuildRequires:  go(k8s.io/apimachinery/pkg/api/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/asn1)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/internalversion)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/internalversion/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1beta1)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/meta/v1beta1/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/apis/testapigroup/v1)
BuildRequires:  go(k8s.io/apimachinery/pkg/conversion)
BuildRequires:  go(k8s.io/apimachinery/pkg/fields)
BuildRequires:  go(k8s.io/apimachinery/pkg/labels)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/cbor)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/cbor/direct)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/json)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/protobuf)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/recognizer)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/serializer/streaming)
BuildRequires:  go(k8s.io/apimachinery/pkg/runtime/testing)
BuildRequires:  go(k8s.io/apimachinery/pkg/selection)
BuildRequires:  go(k8s.io/apimachinery/pkg/sharding)
BuildRequires:  go(k8s.io/apimachinery/pkg/types)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/cache)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/diff)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/json)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/managedfields)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/managedfields/managedfieldstest)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/mergepatch)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/net)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/portforward)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/proxy)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/rand)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/remotecommand)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/sort)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/uuid)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/validation/field)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/version)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/waitgroup)
BuildRequires:  go(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires:  go(k8s.io/apimachinery/pkg/watch)
BuildRequires:  go(k8s.io/apimachinery/pkg/version)
BuildRequires:  go(k8s.io/client-go/applyconfigurations)
BuildRequires:  go(k8s.io/client-go/discovery)
BuildRequires:  go(k8s.io/client-go/dynamic)
BuildRequires:  go(k8s.io/client-go/features)
BuildRequires:  go(k8s.io/client-go/informers)
BuildRequires:  go(k8s.io/client-go/kubernetes)
BuildRequires:  go(k8s.io/client-go/listers)
BuildRequires:  go(k8s.io/client-go/openapi)
BuildRequires:  go(k8s.io/client-go/rest)
BuildRequires:  go(k8s.io/client-go/restmapper)
BuildRequires:  go(k8s.io/client-go/testing)
BuildRequires:  go(k8s.io/client-go/tools/cache)
BuildRequires:  go(k8s.io/client-go/tools/cache/synctrack)
BuildRequires:  go(k8s.io/client-go/tools/clientcmd)
BuildRequires:  go(k8s.io/client-go/tools/clientcmd/api)
BuildRequires:  go(k8s.io/client-go/tools/clientcmd/api/v1)
BuildRequires:  go(k8s.io/client-go/tools/events)
BuildRequires:  go(k8s.io/client-go/tools/portforward)
BuildRequires:  go(k8s.io/client-go/tools/remotecommand)
BuildRequires:  go(k8s.io/client-go/transport)
BuildRequires:  go(k8s.io/client-go/util/cert)
BuildRequires:  go(k8s.io/client-go/util/consistencydetector)
BuildRequires:  go(k8s.io/client-go/util/exec)
BuildRequires:  go(k8s.io/client-go/util/flowcontrol)
BuildRequires:  go(k8s.io/client-go/util/keyutil)
BuildRequires:  go(k8s.io/client-go/util/retry)
BuildRequires:  go(k8s.io/client-go/util/testing)
BuildRequires:  go(k8s.io/client-go/util/watchlist)
BuildRequires:  go(k8s.io/client-go/util/workqueue)
BuildRequires:  go(k8s.io/component-base/cli)
BuildRequires:  go(k8s.io/component-base/compatibility)
BuildRequires:  go(k8s.io/component-base/featuregate)
BuildRequires:  go(k8s.io/component-base/logs)
BuildRequires:  go(k8s.io/component-base/metrics)
BuildRequires:  go(k8s.io/component-base/tracing)
BuildRequires:  go(k8s.io/component-base/version)
BuildRequires:  go(k8s.io/component-base/zpages/features)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kms/apis/v1beta1)
BuildRequires:  go(k8s.io/kms/apis/v2)
BuildRequires:  go(k8s.io/kms/pkg/service)
BuildRequires:  go(k8s.io/kms/pkg/util)
BuildRequires:  go(k8s.io/kube-openapi/pkg/builder)
BuildRequires:  go(k8s.io/kube-openapi/pkg/builder3)
BuildRequires:  go(k8s.io/kube-openapi/pkg/common)
BuildRequires:  go(k8s.io/kube-openapi/pkg/common/restfuladapter)
BuildRequires:  go(k8s.io/kube-openapi/pkg/handler)
BuildRequires:  go(k8s.io/kube-openapi/pkg/handler3)
BuildRequires:  go(k8s.io/kube-openapi/pkg/schemamutation)
BuildRequires:  go(k8s.io/kube-openapi/pkg/spec3)
BuildRequires:  go(k8s.io/kube-openapi/pkg/util)
BuildRequires:  go(k8s.io/kube-openapi/pkg/util/proto)
BuildRequires:  go(k8s.io/kube-openapi/pkg/validation/spec)
BuildRequires:  go(k8s.io/kube-openapi/pkg/validation/strfmt)
BuildRequires:  go(k8s.io/streaming/pkg)
BuildRequires:  go(k8s.io/utils/clock)
BuildRequires:  go(k8s.io/utils/dump)
BuildRequires:  go(k8s.io/utils/lru)
BuildRequires:  go(k8s.io/utils/net)
BuildRequires:  go(k8s.io/utils/path)
BuildRequires:  go(k8s.io/utils/ptr)
BuildRequires:  go(k8s.io/utils/third_party/forked/golang/btree)
BuildRequires:  go(sigs.k8s.io/apiserver-network-proxy/konnectivity-client)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6/value)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go-rpm-macros

Provides:       go(k8s.io/apiserver) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/configuration) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/initializer) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/authorizer) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/cel) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/manifest) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/manifest/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/namespace/lifecycle) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/config) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/config/apis/policyconfig) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/config/apis/policyconfig/install) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/config/apis/policyconfig/v1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/generic) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/internal/generic) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/manifest/loader) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/manifest/source) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/matching) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/mutating) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/mutating/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/mutating/patch) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/validating) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/policy/validating/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/resourcequota) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/resourcequota/apis/resourcequota) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/resourcequota/apis/resourcequota/install) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/resourcequota/apis/resourcequota/v1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/resourcequota/apis/resourcequota/v1alpha1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/resourcequota/apis/resourcequota/v1beta1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/resourcequota/apis/resourcequota/validation) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/config) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/config/apis/webhookadmission) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/config/apis/webhookadmission/install) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/config/apis/webhookadmission/v1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/errors) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/generic) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/initializer) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/manifest/loader) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/manifest/source) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/matchconditions) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/mutating) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/predicates/namespace) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/predicates/object) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/predicates/rules) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/request) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/testcerts) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/util) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/plugin/webhook/validating) = %{version}
Provides:       go(k8s.io/apiserver/pkg/admission/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/apidiscovery/v2) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/apidiscovery/v2beta1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/apiserver) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/apiserver/install) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/apiserver/load) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/apiserver/v1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/apiserver/v1alpha1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/apiserver/v1beta1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/apiserver/validation) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/audit) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/audit/fuzzer) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/audit/install) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/audit/v1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/audit/validation) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/cel) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/example) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/example/fuzzer) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/example/install) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/example/v1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/example2) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/example2/install) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/example2/v1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/apis/flowcontrol/bootstrap) = %{version}
Provides:       go(k8s.io/apiserver/pkg/audit) = %{version}
Provides:       go(k8s.io/apiserver/pkg/audit/policy) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/authenticator) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/authenticatorfactory) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/cel) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/group) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/request/anonymous) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/request/bearertoken) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/request/headerrequest) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/request/union) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/request/websocket) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/request/x509) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/serviceaccount) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/token/cache) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/token/jwt) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/token/tokenfile) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/token/union) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authentication/user) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authorization/authorizer) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authorization/authorizerfactory) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authorization/cel) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authorization/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authorization/path) = %{version}
Provides:       go(k8s.io/apiserver/pkg/authorization/union) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel/common) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel/environment) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel/lazy) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel/library) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel/mutation) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel/mutation/dynamic) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel/openapi) = %{version}
Provides:       go(k8s.io/apiserver/pkg/cel/openapi/resolver) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/deprecation) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/discovery) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/discovery/aggregated) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/filterlatency) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/filters) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/filters/impersonation) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/filters/impersonation/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/handlers) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/handlers/fieldmanager) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/handlers/finisher) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/handlers/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/handlers/negotiation) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/handlers/responsewriters) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/openapi) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/openapi/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/request) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/responsewriter) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/endpoints/warning) = %{version}
Provides:       go(k8s.io/apiserver/pkg/features) = %{version}
Provides:       go(k8s.io/apiserver/pkg/quota/v1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/quota/v1/generic) = %{version}
Provides:       go(k8s.io/apiserver/pkg/reconcilers) = %{version}
Provides:       go(k8s.io/apiserver/pkg/registry) = %{version}
Provides:       go(k8s.io/apiserver/pkg/registry/generic) = %{version}
Provides:       go(k8s.io/apiserver/pkg/registry/generic/registry) = %{version}
Provides:       go(k8s.io/apiserver/pkg/registry/generic/rest) = %{version}
Provides:       go(k8s.io/apiserver/pkg/registry/generic/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/registry/rest) = %{version}
Provides:       go(k8s.io/apiserver/pkg/registry/rest/resttest) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/dynamiccertificates) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/egressselector) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/egressselector/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/filters) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/flagz) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/flagz/api/v1alpha1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/flagz/api/v1beta1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/flagz/negotiate) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/flagz/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/healthz) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/httplog) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/mux) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/options) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/options/authenticationconfig/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/options/authorizationconfig/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/options/encryptionconfig) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/options/encryptionconfig/controller) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/options/encryptionconfig/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/resourceconfig) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/routes) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/routine) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/statusz) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/statusz/api/v1alpha1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/statusz/api/v1beta1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/statusz/negotiate) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/statusz/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/server/storage) = %{version}
Provides:       go(k8s.io/apiserver/pkg/sharding) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/cacher) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/cacher/delegator) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/cacher/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/cacher/progress) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/cacher/store) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/cacher/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/errors) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/etcd3) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/etcd3/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/etcd3/preflight) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/etcd3/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/etcd3/testing/testingcert) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/etcd3/testserver) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/feature) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/names) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/storagebackend) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/storagebackend/factory) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/testresource) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value/encrypt/aes) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value/encrypt/envelope) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value/encrypt/envelope/kmsv2) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value/encrypt/envelope/kmsv2/v2) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value/encrypt/envelope/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value/encrypt/envelope/testing/v1beta1) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value/encrypt/envelope/testing/v2) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value/encrypt/identity) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storage/value/encrypt/secretbox) = %{version}
Provides:       go(k8s.io/apiserver/pkg/storageversion) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/apihelpers) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/compatibility) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/configmetrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/dryrun) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/feature) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/filesystem) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/counter) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/debug) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/eventclock) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/promise) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/testing) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/testing/eventclock) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/testing/promise) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/format) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flowcontrol/request) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/flushwriter) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/notfoundhandler) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/openapi) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/peerproxy) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/peerproxy/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/proxy) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/proxy/metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/responsewriter) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/shufflesharding) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/webhook) = %{version}
Provides:       go(k8s.io/apiserver/pkg/util/x509metrics) = %{version}
Provides:       go(k8s.io/apiserver/pkg/validation) = %{version}
Provides:       go(k8s.io/apiserver/pkg/warning) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/audit) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/audit/buffered) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/audit/fake) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/audit/log) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/audit/truncate) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/audit/webhook) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/authenticator) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/authenticator/token/oidc) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/authenticator/token/tokentest) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/authenticator/token/webhook) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/authorizer/webhook) = %{version}
Provides:       go(k8s.io/apiserver/plugin/pkg/authorizer/webhook/metrics) = %{version}

Requires:       go(github.com/blang/semver/v4)
Requires:       go(github.com/coreos/go-oidc)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/emicklei/go-restful/v3)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/google/cel-go)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/grpc-ecosystem/go-grpc-middleware)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/mxk/go-flowrate)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.etcd.io/etcd/api/v3)
Requires:       go(go.etcd.io/etcd/client/v3)
Requires:       go(go.etcd.io/etcd/server/v3)
Requires:       go(go.opentelemetry.io/contrib/instrumentation)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/attribute)
Requires:       go(go.opentelemetry.io/otel/exporters)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/semconv/v1.12.0)
Requires:       go(go.opentelemetry.io/otel/semconv/v1.17.0)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/zap)
Requires:       go(go.uber.org/zap/zapcore)
Requires:       go(go.uber.org/zap/zaptest)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/genproto/googleapis)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/credentials)
Requires:       go(google.golang.org/grpc/grpclog)
Requires:       go(google.golang.org/grpc/metadata)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/runtime)
Requires:       go(google.golang.org/protobuf/types)
Requires:       go(gopkg.in/evanphx/json-patch.v4)
Requires:       go(gopkg.in/go-jose/go-jose.v2)
Requires:       go(gopkg.in/natefinch/lumberjack.v2)
Requires:       go(k8s.io/api/admission/v1)
Requires:       go(k8s.io/api/admission/v1beta1)
Requires:       go(k8s.io/api/admissionregistration/v1)
Requires:       go(k8s.io/api/apidiscovery/v2)
Requires:       go(k8s.io/api/apidiscovery/v2beta1)
Requires:       go(k8s.io/api/apiserverinternal/v1alpha1)
Requires:       go(k8s.io/api/authentication/v1)
Requires:       go(k8s.io/api/authentication/v1beta1)
Requires:       go(k8s.io/api/authorization/v1)
Requires:       go(k8s.io/api/authorization/v1beta1)
Requires:       go(k8s.io/api/coordination/v1)
Requires:       go(k8s.io/api/core/v1)
Requires:       go(k8s.io/api/discovery/v1)
Requires:       go(k8s.io/api/flowcontrol/v1)
Requires:       go(k8s.io/apimachinery/pkg/api/apitesting)
Requires:       go(k8s.io/apimachinery/pkg/api/apitesting/fuzzer)
Requires:       go(k8s.io/apimachinery/pkg/api/apitesting/roundtrip)
Requires:       go(k8s.io/apimachinery/pkg/api/equality)
Requires:       go(k8s.io/apimachinery/pkg/api/errors)
Requires:       go(k8s.io/apimachinery/pkg/api/meta)
Requires:       go(k8s.io/apimachinery/pkg/api/operation)
Requires:       go(k8s.io/apimachinery/pkg/api/resource)
Requires:       go(k8s.io/apimachinery/pkg/api/validate/content)
Requires:       go(k8s.io/apimachinery/pkg/api/validation)
Requires:       go(k8s.io/apimachinery/pkg/apis/asn1)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion/validation)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1/validation)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1beta1)
Requires:       go(k8s.io/apimachinery/pkg/apis/meta/v1beta1/validation)
Requires:       go(k8s.io/apimachinery/pkg/apis/testapigroup/v1)
Requires:       go(k8s.io/apimachinery/pkg/conversion)
Requires:       go(k8s.io/apimachinery/pkg/fields)
Requires:       go(k8s.io/apimachinery/pkg/labels)
Requires:       go(k8s.io/apimachinery/pkg/runtime)
Requires:       go(k8s.io/apimachinery/pkg/runtime/schema)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor/direct)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/json)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/protobuf)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/recognizer)
Requires:       go(k8s.io/apimachinery/pkg/runtime/serializer/streaming)
Requires:       go(k8s.io/apimachinery/pkg/runtime/testing)
Requires:       go(k8s.io/apimachinery/pkg/selection)
Requires:       go(k8s.io/apimachinery/pkg/sharding)
Requires:       go(k8s.io/apimachinery/pkg/types)
Requires:       go(k8s.io/apimachinery/pkg/util/cache)
Requires:       go(k8s.io/apimachinery/pkg/util/diff)
Requires:       go(k8s.io/apimachinery/pkg/util/errors)
Requires:       go(k8s.io/apimachinery/pkg/util/intstr)
Requires:       go(k8s.io/apimachinery/pkg/util/json)
Requires:       go(k8s.io/apimachinery/pkg/util/managedfields)
Requires:       go(k8s.io/apimachinery/pkg/util/managedfields/managedfieldstest)
Requires:       go(k8s.io/apimachinery/pkg/util/mergepatch)
Requires:       go(k8s.io/apimachinery/pkg/util/net)
Requires:       go(k8s.io/apimachinery/pkg/util/portforward)
Requires:       go(k8s.io/apimachinery/pkg/util/proxy)
Requires:       go(k8s.io/apimachinery/pkg/util/rand)
Requires:       go(k8s.io/apimachinery/pkg/util/remotecommand)
Requires:       go(k8s.io/apimachinery/pkg/util/runtime)
Requires:       go(k8s.io/apimachinery/pkg/util/sets)
Requires:       go(k8s.io/apimachinery/pkg/util/sort)
Requires:       go(k8s.io/apimachinery/pkg/util/strategicpatch)
Requires:       go(k8s.io/apimachinery/pkg/util/uuid)
Requires:       go(k8s.io/apimachinery/pkg/util/validation)
Requires:       go(k8s.io/apimachinery/pkg/util/validation/field)
Requires:       go(k8s.io/apimachinery/pkg/util/version)
Requires:       go(k8s.io/apimachinery/pkg/util/wait)
Requires:       go(k8s.io/apimachinery/pkg/util/waitgroup)
Requires:       go(k8s.io/apimachinery/pkg/util/yaml)
Requires:       go(k8s.io/apimachinery/pkg/watch)
Requires:       go(k8s.io/apimachinery/pkg/version)
Requires:       go(k8s.io/client-go/applyconfigurations)
Requires:       go(k8s.io/client-go/discovery)
Requires:       go(k8s.io/client-go/dynamic)
Requires:       go(k8s.io/client-go/informers)
Requires:       go(k8s.io/client-go/kubernetes)
Requires:       go(k8s.io/client-go/listers)
Requires:       go(k8s.io/client-go/openapi)
Requires:       go(k8s.io/client-go/rest)
Requires:       go(k8s.io/client-go/restmapper)
Requires:       go(k8s.io/client-go/testing)
Requires:       go(k8s.io/client-go/tools/cache)
Requires:       go(k8s.io/client-go/tools/cache/synctrack)
Requires:       go(k8s.io/client-go/tools/clientcmd)
Requires:       go(k8s.io/client-go/tools/clientcmd/api)
Requires:       go(k8s.io/client-go/tools/clientcmd/api/v1)
Requires:       go(k8s.io/client-go/tools/events)
Requires:       go(k8s.io/client-go/tools/portforward)
Requires:       go(k8s.io/client-go/tools/remotecommand)
Requires:       go(k8s.io/client-go/transport)
Requires:       go(k8s.io/client-go/util/cert)
Requires:       go(k8s.io/client-go/util/consistencydetector)
Requires:       go(k8s.io/client-go/util/exec)
Requires:       go(k8s.io/client-go/util/flowcontrol)
Requires:       go(k8s.io/client-go/util/keyutil)
Requires:       go(k8s.io/client-go/util/retry)
Requires:       go(k8s.io/client-go/util/testing)
Requires:       go(k8s.io/client-go/util/watchlist)
Requires:       go(k8s.io/client-go/util/workqueue)
Requires:       go(k8s.io/component-base/cli)
Requires:       go(k8s.io/component-base/compatibility)
Requires:       go(k8s.io/component-base/featuregate)
Requires:       go(k8s.io/component-base/logs)
Requires:       go(k8s.io/component-base/metrics)
Requires:       go(k8s.io/component-base/tracing)
Requires:       go(k8s.io/component-base/version)
Requires:       go(k8s.io/component-base/zpages/features)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kms/apis/v1beta1)
Requires:       go(k8s.io/kms/apis/v2)
Requires:       go(k8s.io/kms/pkg/service)
Requires:       go(k8s.io/kms/pkg/util)
Requires:       go(k8s.io/kube-openapi/pkg/builder)
Requires:       go(k8s.io/kube-openapi/pkg/builder3)
Requires:       go(k8s.io/kube-openapi/pkg/common)
Requires:       go(k8s.io/kube-openapi/pkg/common/restfuladapter)
Requires:       go(k8s.io/kube-openapi/pkg/handler)
Requires:       go(k8s.io/kube-openapi/pkg/handler3)
Requires:       go(k8s.io/kube-openapi/pkg/schemamutation)
Requires:       go(k8s.io/kube-openapi/pkg/spec3)
Requires:       go(k8s.io/kube-openapi/pkg/util)
Requires:       go(k8s.io/kube-openapi/pkg/util/proto)
Requires:       go(k8s.io/kube-openapi/pkg/validation/spec)
Requires:       go(k8s.io/kube-openapi/pkg/validation/strfmt)
Requires:       go(k8s.io/streaming/pkg)
Requires:       go(k8s.io/utils/clock)
Requires:       go(k8s.io/utils/lru)
Requires:       go(k8s.io/utils/net)
Requires:       go(k8s.io/utils/path)
Requires:       go(k8s.io/utils/ptr)
Requires:       go(k8s.io/utils/third_party/forked/golang/btree)
Requires:       go(sigs.k8s.io/apiserver-network-proxy/konnectivity-client)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6/value)
Requires:       go(sigs.k8s.io/yaml)

%description
This package provides the generic Kubernetes API server libraries, including
authentication, authorization, admission, and storage support.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
